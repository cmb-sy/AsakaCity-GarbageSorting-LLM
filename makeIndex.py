import sys
from langchain_community.document_loaders import CSVLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings

def load_document(filename):
    loader = CSVLoader(filename, autodetect_encoding=True)
    pages = loader.load()
    python_splitter = RecursiveCharacterTextSplitter(chunk_size=2000, chunk_overlap=400)
    splits = python_splitter.split_documents(pages)
    Chroma.from_documents(
        documents=splits,
        embedding=OpenAIEmbeddings(model="text-embedding-3-small"),
        persist_directory="data",
    )


load_document(sys.argv[1])