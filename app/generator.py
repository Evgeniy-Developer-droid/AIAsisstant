import requests
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_openai.embeddings import OpenAIEmbeddings
import weaviate
from weaviate.embedded import EmbeddedOptions
from dotenv import load_dotenv
from langchain_weaviate.vectorstores import WeaviateVectorStore
from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain.schema.runnable import RunnablePassthrough
from langchain.schema.output_parser import StrOutputParser

load_dotenv()

template = """You are an assistant who helps write a clear 
proposal for an Upwork task posted by a client. 
Based on the job description, you must write an excellent proposal text, taking into account technology, 
and briefly describe how you see the solution to the problem or the path to creating the project.
Question: {question} 
Answer:
"""
prompt = ChatPromptTemplate.from_template(template)

llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)

rag_chain = (
    {"question": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)

def generate_proposal(question: str):
    try:
        res = rag_chain.invoke(question)
        return res
    except Exception as e:
        print(f"Error generating proposal - {e}")
        return "No proposal generated try again later"