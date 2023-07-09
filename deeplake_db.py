from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.docstore.document import Document
from langchain.vectorstores import DeepLake
from langchain.embeddings.openai import OpenAIEmbeddings

def load_db(file_name: str, my_activeloop_org_id: str, database_name: str):
    
    # Load the texts from a file
    with open(file_name) as f:
        text = f.read()

    # Split the documents
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000, chunk_overlap=0, separators=[" ", ",", "\n"]
    )
    texts = text_splitter.split_text(text)
    
    # Create Document objects from the split texts
    docs = [Document(page_content=t) for t in texts]
    
    # Create OpenAI Embeddings instance
    embeddings = OpenAIEmbeddings(model='text-embedding-ada-002')
    
    # Set the organization ID and dataset name for DeepLake
    my_activeloop_org_id = my_activeloop_org_id
    my_activeloop_dataset_name = database_name
    
    # Define the dataset path
    dataset_path = f"hub://{my_activeloop_org_id}/{my_activeloop_dataset_name}"
    
    # Create a DeepLake vector store with the dataset path and embedding function
    db = DeepLake(dataset_path=dataset_path, embedding_function=embeddings)
    
    # Add the documents to the DeepLake vector store
    db.add_documents(docs)
    
    return db
