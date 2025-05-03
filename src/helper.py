import os
from langchain.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings


def load_pdf_file(data_folder):
    """Load PDF documents from a directory."""
    if not os.path.exists(data_folder):
        raise FileNotFoundError(f"Directory not found: {data_folder}")
    
    print(f"Looking for PDFs in: {data_folder}")
    loader = DirectoryLoader(data_folder, glob="*.pdf", loader_cls=PyPDFLoader)
    documents = loader.load()

    print(f"✅ Loaded {len(documents)} document(s).")
    return documents


def text_split(extracted_data):
    """Split the extracted documents into smaller text chunks."""
    print("🔄 Splitting text into chunks...")
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=20)
    text_chunks = text_splitter.split_documents(extracted_data)

    print(f"✅ Created {len(text_chunks)} text chunk(s).")
    return text_chunks


def download_hugging_face_embeddings():
    """Load HuggingFace sentence transformer embeddings."""
    print("⬇️ Downloading HuggingFace embeddings model...")
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    print("✅ Embeddings loaded.")
    return embeddings


# For direct testing of this file
if __name__ == "__main__":
    try:
        folder_path = "./data"  # change this to the actual path where your PDFs are stored
        documents = load_pdf_file(folder_path)
        chunks = text_split(documents)
        embeddings = download_hugging_face_embeddings()
        
        # Optional: embed first chunk just to show it's working
        if chunks:
            sample = chunks[0].page_content
            embedded = embeddings.embed_query(sample)
            print(f"✅ Sample embedding generated (first 5 dims): {embedded[:5]}")

    except Exception as e:
        print("❌ Error:", e)
