# Import necessary modules and classes
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA

# Define the 'summarizer' function
def summarizer(db, query:str):
    # Create a retriever using the provided 'db'
    retriever = db.as_retriever()
    
    # Set search parameters for the retriever
    retriever.search_kwargs['distance_metric'] = 'cos'
    retriever.search_kwargs['k'] = 4
    
    # Create an instance of the OpenAI language model
    llm = OpenAI(temperature = 0)
    
    # Define the template for the prompt
    prompt_template = """Use the following pieces of transcripts from a video to answer the question in bullet points and summarized. If you don't know the answer, just say that you don't know, don't try to make up an answer.
    {context}
    Question: {question}
    Summarized answer in bullet points:"""
    
    # Create a PromptTemplate object using the template
    PROMPT = PromptTemplate(
        template=prompt_template, input_variables=["context", "question"]
    )
    
    # Define chain type-specific kwargs
    chain_type_kwargs = {"prompt": PROMPT}
    
    # Create a RetrievalQA instance using the language model, retriever, and chain type kwargs
    qa = RetrievalQA.from_chain_type(llm=llm,
                                 chain_type="map_reduce",
                                 retriever=retriever,
                                 chain_type_kwargs=chain_type_kwargs)
    
    # Run the query using the RetrievalQA instance
    return qa.run(query)
