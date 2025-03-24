import streamlit as st

def apply_styles():
    """
    アプリケーションにCSSスタイルを適用する関数
    """
    # ページの基本設定とスタイルを適用
    st.set_page_config(
        page_title="マルチモーダルRAGチャット",
        page_icon="🤖",
        layout="wide",
    )
    
    # CSSスタイルの追加
    st.markdown("""
    <style>
        .main-header {
            font-size: 2.5rem;
            color: #4527A0;
            text-align: center;
            margin-bottom: 1rem;
            font-weight: 600;
        }
        .subheader {
            font-size: 1.5rem;
            color: #5E35B1;
            margin-bottom: 1rem;
            font-weight: 500;
        }
        .chat-container {
            border-radius: 10px;
            padding: 10px;
            background-color: #F5F5F5;
            margin-bottom: 15px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        }
        .user-message {
            background-color: #E3F2FD;
            padding: 10px 15px;
            border-radius: 15px 15px 15px 0;
            margin: 10px 0;
            border-left: 4px solid #2196F3;
            display: flex;
            align-items: center;
        }
        .bot-message {
            background-color: #E8F5E9;
            padding: 10px 15px;
            border-radius: 15px 15px 0 15px;
            margin: 10px 0;
            border-left: 4px solid #4CAF50;
            display: flex;
            align-items: center;
        }
        .message-avatar {
            font-size: 1.5rem;
            margin-right: 10px;
        }
        .message-text {
            flex-grow: 1;
        }
        .stButton button {
            background-color: #673AB7;
            color: white;
            font-weight: 500;
            padding: 0.5rem 1rem;
            border-radius: 5px;
            border: none;
            transition: all 0.3s;
        }
        .stButton button:hover {
            background-color: #5E35B1;
            box-shadow: 0 4px 8px rgba(0,0,0,0.2);
            transform: translateY(-2px);
        }
        .info-box {
            background-color: #EDE7F6;
            border-radius: 8px;
            padding: 15px;
            margin-top: 20px;
            border-left: 5px solid #673AB7;
        }
        .stTextInput input {
            border-radius: 5px;
            border: 1px solid #BDBDBD;
            padding: 10px;
        }
        .stTextInput input:focus {
            border-color: #673AB7;
            box-shadow: 0 0 0 2px rgba(103, 58, 183, 0.2);
        }
        .upload-section {
            background-color: #F3E5F5;
            padding: 15px;
            border-radius: 8px;
            margin-bottom: 20px;
        }
        .sidebar-section {
            margin-bottom: 30px;
        }
        .stAlert {
            background-color: #D1C4E9;
            color: #4527A0;
        }
    </style>
    """, unsafe_allow_html=True)

def display_app_info():
    """
    アプリケーションの情報を表示する関数
    """
    st.markdown("""
    ### ℹ️ アプリについて
    
    このアプリは以下の機能を提供します：
    
    - 💬 テキストによる質問応答
    - 🖼️ 画像の分析と理解
    - 📚 RAG技術による関連情報検索
    - 🔄 マルチターン会話
    """)
    
def display_footer():
    """
    フッターを表示する関数
    """
    st.markdown("""
    <div style="text-align: center; margin-top: 30px; color: #9E9E9E; font-size: 0.8rem;">
        © 2023 マルチモーダルRAGチャットボット | Powered by LangChain & Streamlit
    </div>
    """, unsafe_allow_html=True) 