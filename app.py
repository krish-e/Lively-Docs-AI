import os
from dotenv import load_dotenv
from langchain_openai.chat_models import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain.prompts import ChatPromptTemplate
from langchain_community.document_loaders import PyPDFLoader
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import DocArrayInMemorySearch    
from langchain_core.runnables import RunnableParallel, RunnablePassthrough

load_dotenv()
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

model = ChatOpenAI(openai_api_key=OPENAI_API_KEY, model='gpt-3.5-turbo')
parser = StrOutputParser()

# Fixing the prompt template to give both context and question to the model
template = """
Answer the question based on the context below. If you can't answer the question, reply "I'm not sure if the document has context for this question."
    
Context: {context}
    
Question: {question}
"""
prompt = ChatPromptTemplate.from_template(template)

# Replace file_path with the URL fo your document(local or online). Except google drive
print("\nLively Docs AI")
file_path = input("AI: Enter document's URL(local or online source except Google Drive):\nYou: ")

# Splitting Book into small chunks
loader = PyPDFLoader(file_path)
pages = loader.load_and_split()
pages

# Loading book to the vector store(local memory)
embeddings = OpenAIEmbeddings() 
vector_store = DocArrayInMemorySearch.from_documents(pages, embeddings)

setup = RunnableParallel(context= vector_store.as_retriever(), question=RunnablePassthrough())
chain = setup | prompt | model | parser

exit_keywords = ['nothing', 'no', 'exit']
question = input("AI: Ask any question based on your document content (reply 'exit' to end session): \nYou: ")
while True:
    if not question.lower() in exit_keywords:
        print(chain.invoke(question))
    else:
        break
    question = input("\nAI: Next Question?\nYou: ")
    
