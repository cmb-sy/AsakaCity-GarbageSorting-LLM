import base64
import os

import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
from operator import itemgetter
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")

if not API_KEY:
    st.error("APIキーが設定されていません。環境変数にAPIキーを設定してください。")
    st.stop()

# 画像の説明を取得
def get_image_description(image_data: str):
    try:
        prompt = ChatPromptTemplate.from_messages(
            [
                (
                    "human",
                    [
                        {
                            "type": "image_url",
                            "image_url": {"url": f"data:image/jpeg;base64,{image_data}"},
                        }
                    ],
                ),
            ]
        )
        chain = prompt | ChatOpenAI(model="gpt-4o-mini", api_key=API_KEY) | StrOutputParser()
        return chain.invoke({"image_data": image_data})
    except Exception as e:
        st.error(f"画像の説明取得中にエラーが発生しました: {e}")
        return ""

# メッセージを作成
def create_message(dic: dict):
    image_data = dic.get("image")
    if image_data:
        return [
            (
                "human",
                [
                    {"type": "text", "text": dic["input"]},
                    {
                        "type": "image_url",
                        "image_url": {"url": f"data:image/jpeg;base64,{image_data}"},
                    },
                ],
            )
        ]
    return [("human", dic["input"])]

# ドキュメントを整形
def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

# チェーンを作成
def create_chain():
    try:
        vectorstore = Chroma(
            embedding_function=OpenAIEmbeddings(model="text-embedding-3-small", api_key=API_KEY),
            persist_directory="data",
        )
        retriever = vectorstore.as_retriever(search_kwargs={"k": 3})
        prompt = ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    "回答には以下の情報も参考にしてください。参考情報：\n{info}",
                ),
                ("placeholder", "{history}"),
                ("placeholder", "{message}"),
            ]
        )
        return (
            {
                "message": create_message,
                "info": itemgetter("input") | retriever | format_docs,
                "history": itemgetter("history"),
            }
            | prompt
            | ChatOpenAI(model="gpt-4o-mini", temperature=0, api_key=API_KEY)
        )
    except Exception as e:
        st.error(f"チェーン作成中にエラーが発生しました: {e}")
        st.stop()

# セッション状態を初期化
if "history" not in st.session_state:
    st.session_state.history = []
    st.session_state.chain = create_chain()

st.title("マルチモーダルRAGチャットボット")

# 画像アップローダ
uploaded_file = st.file_uploader("画像を選択してください", type=["jpg", "jpeg", "png"])

# アップロードされた画像を表示
if uploaded_file is not None:
    st.image(uploaded_file, caption="画像", width=300)

# ユーザ入力
user_input = st.text_input("メッセージを入力してください:")

# ボタンをクリックしたときの処理
if st.button("送信"):
    try:
        image_data = None
        image_description = ""
        if uploaded_file is not None:
            image_data = base64.b64encode(uploaded_file.read()).decode("utf-8")
            image_description = get_image_description(image_data)
        
        # チェーンを実行
        response = st.session_state.chain.invoke(
            {
                "input": user_input + image_description,
                "history": st.session_state.history,
                "image": image_data,
            }
        )
        st.session_state.history.append(HumanMessage(user_input))
        st.session_state.history.append(response)

        # 会話履歴を表示
        for message in reversed(st.session_state.history):
            st.write(f"{message.type}: {message.content}")
    except Exception as e:
        st.error(f"処理中にエラーが発生しました: {e}")