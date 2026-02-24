from langchain_community.document_loaders import YoutubeLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_community.vectorstores import FAISS
from langchain_groq import ChatGroq
from langchain_community.embeddings import HuggingFaceEmbeddings
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

try:
    # Initialize embeddings with correct model name
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
except ImportError:
    raise ImportError(
        "Could not import sentence-transformers. "
        "Please install it with: pip install sentence-transformers"
    )

def create_vector_db_from_youtube_url(video_url: str) -> FAISS:
    """Create vector database from YouTube video transcript"""
    loader = YoutubeLoader.from_youtube_url(video_url)
    transcript = loader.load()
    
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=100
    )
    docs = text_splitter.split_documents(transcript)
    
    db = FAISS.from_documents(docs, embeddings)
    return db

def get_response_from_query(db, query: str, k: int = 4) -> str:
    """Get response from vector database query using Groq"""
    docs = db.similarity_search(query, k=k)
    docs_page_content = " ".join([d.page_content for d in docs])
    
    llm = ChatGroq(
        temperature=0.7,
        model_name="llama3-70b-8192",
        api_key=os.getenv("GROQ_API_KEY")
    )
    
    prompt = PromptTemplate(
        input_variables=["question", "docs"],
        template="""You are a helpful YouTube assistant that can answer questions 
        about videos based on the video's transcript.
        
        Answer the following question: {question}
        By searching the following video transcript: {docs}
        
        Only use the factual information from the transcript.
        If you don't have enough information, say 'I don't know'.
        Provide detailed answers."""
    )
    
    chain = LLMChain(llm=llm, prompt=prompt)
    response = chain.run(question=query, docs=docs_page_content)
    return response.strip()

if __name__ == "__main__":
    video_url = "https://www.youtube.com/watch?v=OscaZ2av4Y"
    
    try:
        print("Creating vector database from YouTube video...")
        db = create_vector_db_from_youtube_url(video_url)
        
        while True:
            query = input("\nYour question (or 'exit' to quit): ")
            if query.lower() == 'exit':
                break
            print(f"\nAnswer: {get_response_from_query(db, query)}")
            
    except Exception as e:
        print(f"Error: {e}")