from search import search_prompt
from langchain.chat_models import init_chat_model
from langchain_postgres import PGVector
import os
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

def main():
    pg_vector = PGVector(
        embeddings=GoogleGenerativeAIEmbeddings(model=os.getenv("GOOGLE_EMBEDDING_MODEL", "models/gemini-embedding-001")),
        collection_name=os.getenv("PG_VECTOR_COLLECTION_NAME"),
        connection=os.getenv("DATABASE_URL"),
        use_jsonb=True
        )
    llm = init_chat_model(model="gemini-2.5-flash", model_provider="google_genai")
    chain = search_prompt() | llm
    
    print("Chat iniciado! Digite 'sair' para encerrar.")
    
    while True:
        question = input("\nFaça sua pergunta: ")
        
        if question.lower() in ['sair']:
            print("Encerrando chat...")
            break
            
        if question.strip() == "":
            print("Por favor, digite uma pergunta válida.")
            continue
            
        try:
            context = pg_vector.similarity_search_with_score(question, k=10)
            response = chain.invoke({"contexto": context, "pergunta": question})
            print(f"\nResposta: {response.content}")
        except Exception as e:
            print(f"Erro ao processar pergunta: {e}")
            print("Tente novamente.")
    
if __name__ == "__main__":
    main()