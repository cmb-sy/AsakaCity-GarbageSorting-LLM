import sys
import streamlit as st
from langchain_core.messages import HumanMessage

sys.path.append("../")

from multimodal_chat.utils.image_processing import get_image_description, encode_image
from multimodal_chat.utils.message_handling import display_message
from multimodal_chat.utils.rag_chain import create_chain
from multimodal_chat.components.styles import apply_styles, display_app_info, display_footer

def main():
    """
    マルチモーダルRAGチャットアプリケーションのメイン関数
    """
    # スタイルを適用
    apply_styles()
    
    # セッション状態の初期化
    if "history" not in st.session_state:
        st.session_state.history = []  # チャット履歴を初期化
        st.session_state.chain = create_chain()  # チェーンを作成
        st.session_state.last_input = ""  # 最後の入力を初期化

    # マルチモーダルRAGチャットのヘッダー
    st.markdown('<div class="main-header">🤖 マルチモーダルRAGチャットボット</div>', unsafe_allow_html=True)

    # 2カラムレイアウトを作成
    main_col, side_col = st.columns([3, 1])

    # サイドカラムの内容
    with side_col:
        st.markdown('<div class="subheader">⚙️ 設定</div>', unsafe_allow_html=True)
        
        # 画像アップロードセクション
        st.markdown('<div class="sidebar-section">', unsafe_allow_html=True)
        st.markdown('<div class="upload-section">', unsafe_allow_html=True)
        uploaded_file = st.file_uploader("📷 画像をアップロード", type=["jpg", "jpeg", "png", "gif"])
        
        if uploaded_file is not None:
            # プレビュー画像を表示
            st.image(uploaded_file, caption="アップロードされた画像", use_column_width=True)
            st.success("✅ 画像がアップロードされました")
        st.markdown('</div>', unsafe_allow_html=True)
        
        # アプリ情報
        st.markdown('<div class="info-box">', unsafe_allow_html=True)
        display_app_info()
        st.markdown('</div>', unsafe_allow_html=True)
        
        # 会話履歴リセットボタン
        if st.button("🔄 会話をリセット"):
            st.session_state.history = []  # 履歴をリセット
            st.success("会話履歴をリセットしました！")
        st.markdown('</div>', unsafe_allow_html=True)

    # メインカラムの内容
    with main_col:
        # チャット履歴表示エリア
        st.markdown('<div class="subheader">💬 会話履歴</div>', unsafe_allow_html=True)
        st.markdown('<div class="chat-container">', unsafe_allow_html=True)
        
        # 会話履歴を表示
        chat_placeholder = st.container()
        
        with chat_placeholder:
            for i, msg in enumerate(st.session_state.history):
                # 偶数インデックスはユーザー、奇数インデックスはボット
                is_user = i % 2 == 0
                display_message(msg, is_user=is_user)
        
        st.markdown('</div>', unsafe_allow_html=True)
        
        # 入力フォーム
        st.markdown('<div class="subheader">✏️ メッセージを入力</div>', unsafe_allow_html=True)
        
        # テキスト入力と送信ボタンを横に並べる
        col1, col2 = st.columns([5, 1])
        
        with col1:
            user_input = st.text_input("", placeholder="メッセージを入力してください...", label_visibility="collapsed")
        
        with col2:
            send_pressed = st.button("送信", use_container_width=True)
        
        # 送信ボタンが押されたときの処理
        if send_pressed and user_input:
            # 入力をセッションに保存（ページリロード対策）
            st.session_state.last_input = user_input
            
            # ユーザー入力をチャット履歴に表示
            with chat_placeholder:
                display_message(user_input, is_user=True)
            
            # スピナーを表示しながら応答を生成
            with st.spinner("応答を生成中..."):
                image_data = None
                image_description = ""
                
                # 画像がアップロードされている場合の処理
                if uploaded_file is not None:
                    # 画像をbase64エンコード
                    bytes_data = uploaded_file.getvalue()
                    image_data = encode_image(bytes_data)
                    # 画像の説明を取得
                    image_description = get_image_description(image_data)
                
                # RAGチェーンを呼び出して応答を生成
                response = st.session_state.chain.invoke(
                    {
                        "input": user_input + image_description,  # ユーザー入力と画像説明を結合
                        "history": st.session_state.history,  # 会話履歴
                        "image": image_data  # 画像データ
                    }
                )
                
                # 応答をチャット履歴に追加
                st.session_state.history.append(HumanMessage(user_input))  # ユーザーのメッセージを追加
                st.session_state.history.append(response)  # ボットの応答を追加
                
                # ボットの応答を表示
                with chat_placeholder:
                    display_message(response, is_user=False)
            
            # 入力フィールドをクリア（JavaScriptを使用）
            st.markdown("""
            <script>
                const input = document.querySelector('.stTextInput input');
                if (input) {
                    input.value = '';
                }
            </script>
            """, unsafe_allow_html=True)
            
            # ページをリロードして入力フィールドをクリア
            st.rerun()

    # フッターを表示
    display_footer()

if __name__ == "__main__":
    main() 