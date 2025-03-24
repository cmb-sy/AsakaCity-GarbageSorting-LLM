from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from operator import itemgetter
from multimodal_chat.utils.message_handling import create_message, format_docs

def create_chain():
    """
    RAG（検索拡張生成）チェーンを作成する関数
    
    Returns:
        chain: LangChainの処理パイプライン
    """
    # ベクトルストアの作成（Chroma DBを使用）
    vectorstore = Chroma(
        embedding_function=OpenAIEmbeddings(model="text-embedding-3-small"),
        persist_directory="data",
    )
    
    # 検索時のパラメータを設定（上位3件の関連文書を取得）
    retriever = vectorstore.as_retriever(search_kwargs={"k": 3})
    
    # プロンプトテンプレートの作成
    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "回答には以下の情報も参考にしてください。参考情報：\n{info}",
            ),
            ("placeholder", "{history}"),  # 会話履歴のプレースホルダー
            ("placeholder", "{message}"),  # ユーザーメッセージのプレースホルダー
        ]
    )
    
    # チェーンの作成と返却
    # 1. メッセージ作成、情報検索、履歴取得の各コンポーネントを設定
    # 2. プロンプトテンプレートを適用
    # 3. GPT-4o-miniモデルで応答を生成
    return (
        {
            "message": create_message,  # メッセージ作成関数
            "info": itemgetter("input") | retriever | format_docs,  # 入力から関連情報を検索
            "history": itemgetter("history"),  # 会話履歴を取得
        }
        | prompt  # プロンプトテンプレートを適用
        | ChatOpenAI(model="gpt-4o-mini", temperature=0)  # 応答生成モデル
    ) 