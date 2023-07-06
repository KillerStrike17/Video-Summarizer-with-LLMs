from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.docstore.document import Document
from langchain.vectorstores import DeepLake
from langchain.embeddings.openai import OpenAIEmbeddings

def load_db(file_name,my_activeloop_org_id, database_name):
    
    # Load the texts
    with open(file_name) as f:
        text = f.read()

    # Split the documents
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000, chunk_overlap=0, separators=[" ", ",", "\n"]
        )
    texts = text_splitter.split_text(text)
    
    docs = [Document(page_content=t) for t in texts]
    embeddings = OpenAIEmbeddings(model='text-embedding-ada-002')
    
    # create Deep Lake dataset
    my_activeloop_org_id = my_activeloop_org_id
    my_activeloop_dataset_name = database_name
    dataset_path = f"hub://{my_activeloop_org_id}/{my_activeloop_dataset_name}"

    db = DeepLake(dataset_path=dataset_path, embedding_function=embeddings)
    db.add_documents(docs)
    
    return db