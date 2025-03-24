import base64
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

def get_image_description(image_data: str):
    """
    アップロードされた画像の説明を生成する関数
    
    Args:
        image_data (str): Base64エンコードされた画像データ
        
    Returns:
        str: 画像の説明文
    """
    # 画像プロンプトの作成
    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "human",  # 人間からの入力と認識
                [
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{image_data}"
                        }
                    }
                ]
            )
        ]
    )
    # GPT-4oミニモデルを使って画像の説明を生成
    chain = prompt | ChatOpenAI(model="gpt-4o-mini") | StrOutputParser()
    return chain.invoke({"image_data": image_data})

def encode_image(file_content):
    """
    画像ファイルをBase64エンコードする関数
    
    Args:
        file_content: 画像ファイルのバイトデータ
        
    Returns:
        str: Base64エンコードされた画像データ
    """
    return base64.b64encode(file_content).decode("utf-8") 