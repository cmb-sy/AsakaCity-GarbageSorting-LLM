#!/usr/bin/env python
"""
マルチモーダルRAGチャットアプリケーション起動スクリプト

このスクリプトは、Streamlitアプリケーションを起動するための
シンプルなコマンドラインインターフェースを提供します。
"""

import os
import sys
import subprocess
from dotenv import load_dotenv

def main():
    """
    アプリケーションの起動処理を行うメイン関数
    """
    # .envファイルがあれば読み込む
    load_dotenv()
    
    # OpenAI APIキーの確認
    if not os.environ.get("OPENAI_API_KEY"):
        print("エラー: OPENAI_API_KEYが設定されていません。")
        print("環境変数または.envファイルで設定してください。")
        sys.exit(1)
    
    # アプリケーションのパスを取得
    script_dir = os.path.dirname(os.path.abspath(__file__))
    app_path = os.path.join(script_dir, "app.py")
    
    # Streamlitアプリを起動
    print("マルチモーダルRAGチャットアプリケーションを起動しています...")
    subprocess.run(["streamlit", "run", app_path])

if __name__ == "__main__":
    main()
