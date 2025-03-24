import sys
from langchain_community.document_loaders import CSVLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings

def load_document(filename):
    try:
        # CSVファイルをロード
        loader = CSVLoader(filename, autodetect_encoding=True)
        pages = loader.load()
        print(f"CSVファイル '{filename}' を正常に読み込みました。")

        # テキストを分割
        python_splitter = RecursiveCharacterTextSplitter(chunk_size=2000, chunk_overlap=400)
        splits = python_splitter.split_documents(pages)
        print(f"ドキュメントを {len(splits)} チャンクに分割しました。")


        # Chroma に保存
        Chroma.from_documents(
            documents=splits,
            embedding=OpenAIEmbeddings(model="text-embedding-3-small"),
            persist_directory="data",
        )
        print("データを 'data' ディレクトリに保存しました。")
    except Exception as e:
        print(f"エラーが発生しました: {e}")

if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    filename = "gomi_sorting_garbage.csv"
    print(f"ファイル名が指定されていないため、デフォルトの '{filename}' を使用します。")

load_document(filename)