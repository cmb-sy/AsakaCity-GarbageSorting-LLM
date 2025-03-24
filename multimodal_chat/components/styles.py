import streamlit as st

def apply_styles():
    st.set_page_config(
        page_title="朝霞市ゴミ分別ガイド",
        layout="wide",
    )
    st.markdown("""
                <style>
    .main-header {
        font-size: 2.5rem;
        color: #333333;  // dark grey
        text-align: center;
        margin-bottom: 1rem;
        font-weight: 600;
    }
    .subheader {
        font-size: 1.5rem;
        color: #555555;  // medium grey
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
        background-color: #FFFFFF;
        padding: 10px 15px;
        border-radius: 15px 15px 15px 0;
        margin: 10px 0;
        border-left: 4px solid #B0B0B0;
        display: flex;
        align-items: center;
    }
    .bot-message {
        background-color: #F8F8F8;
        padding: 10px 15px;
        border-radius: 15px 15px 0 15px;
        margin: 10px 0;
        border-left: 4px solid #B0B0B0;
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
        background-color: #E0E0E0;
        color: #333333;
        font-weight: 500;
        padding: 0.5rem 1rem;
        border-radius: 5px;
        border: none;
        transition: all 0.3s;
    }
    .stButton button:hover {
        background-color: #BDBDBD;
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
        transform: translateY(-2px);
    }
    .info-box {
        background-color: #F8F8F8;
        border-radius: 8px;
        padding: 15px;
        margin-top: 20px;
        border-left: 5px solid #B0B0B0;
    }
    .stTextInput input {
        border-radius: 5px;
        border: 1px solid #BDBDBD;
        padding: 10px;
    }
    .stTextInput input:focus {
        border-color: #B0B0B0;
        box-shadow: 0 0 0 2px rgba(176, 176, 176, 0.2);
    }
    .upload-section {
        background-color: #FFFFFF;
        padding: 15px;
        border-radius: 8px;
        margin-bottom: 20px;
    }
    .sidebar-section {
        margin-bottom: 30px;
    }
    .stAlert {
        background-color: #E0E0E0;
        color: #333333;
    }
</style>
""", unsafe_allow_html=True) 