import os
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_postgres import PGVector
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_core.documents import Document

load_dotenv()

PDF_PATH = os.getenv("PDF_PATH")


def pdf_chunk_split(pdf_path: str):
    loader = PyPDFLoader(pdf_path)
    docs = loader.load()
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=150)
    chunks = splitter.split_documents(docs)
    return chunks

def ingest_documents(pg_vector: PGVector, chunks: list[Document]):
    enriched = [
        Document(
            page_content=d.page_content,
            metadata={k:v for k, v in d.metadata.items() if v not in ("", None)}
        )
        for d in chunks
    ]

    ids = [f"doc-{i}" for i in range(len(enriched))]
    pg_vector.add_documents(documents=enriched, ids=ids)


def ingest_pdfs():
    pg_vector = PGVector(
        embeddings=GoogleGenerativeAIEmbeddings(model=os.getenv("GOOGLE_EMBEDDING_MODEL", "models/gemini-embedding-001")),
        collection_name=os.getenv("PG_VECTOR_COLLECTION_NAME"),
        connection=os.getenv("DATABASE_URL"),
        use_jsonb=True
        )

    chunks = pdf_chunk_split(PDF_PATH)
    ingest_documents(pg_vector, chunks)


if __name__ == "__main__":
    ingest_pdfs()