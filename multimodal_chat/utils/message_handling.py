import streamlit as st

def create_message(dic: dict):
    """
    チャットメッセージを作成する関数
    
    Args:
        dic (dict): 入力テキスト、画像データを含む辞書
        
    Returns:
        list: LangChain形式のメッセージリスト
    """
    image_data = dic["image"]
    if image_data:
        # 画像がある場合は、テキストと画像の両方をメッセージに含める
        return [
            (
                "human",
                [
                    {"type": "text", "text": dic["input"]},
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{image_data}"
                        }
                    }
                ]
            )
        ]
    # 画像がない場合は、テキストのみのメッセージを作成
    return [("human", dic["input"])]

def display_message(message, is_user=True):
    """
    チャットメッセージを美しく表示する関数
    
    Args:
        message: 表示するメッセージ (文字列またはHumanMessageオブジェクト)
        is_user: ユーザーのメッセージかどうか (True/False)
    """
    # メッセージの内容を取得
    if hasattr(message, 'content'):
        content = message.content
    else:
        content = message
        
    # メッセージタイプに基づいてスタイルとアイコンを設定
    if is_user:
        message_class = "user-message"
        avatar = "👤"
    else:
        message_class = "bot-message"
        avatar = "🤖"
    
    # HTMLでメッセージを表示
    st.markdown(f"""
    <div class="{message_class}">
        <div class="message-avatar">{avatar}</div>
        <div class="message-text">{content}</div>
    </div>
    """, unsafe_allow_html=True)

def format_docs(docs):
    """
    検索結果の文書を整形する関数
    
    Args:
        docs: 検索結果の文書リスト
        
    Returns:
        str: 改行で結合された文書内容
    """
    formatted_string = ""
    for doc in docs:
        formatted_string += doc.page_content + "\n\n"  # 各ドキュメントの内容を追加
    return formatted_string.strip()  # 最後の改行を削除 