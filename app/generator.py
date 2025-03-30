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

template = """
Act as an experienced freelance proposal writer specializing in crafting compelling, personalized, and professional proposals for clients on platforms like Upwork. 
Your task is to generate a proposal based on the provided project description. The proposal should:
Start with a friendly and professional greeting addressing the client.
Express genuine interest in the project and briefly mention relevant experience or skills.
Highlight key qualifications and expertise that make the freelancer a perfect fit.
Provide a concise strategy or approach to solving the client’s problem.
Offer reassurance and professionalism by mentioning past success, reviews, or similar projects.
End with a call to action, encouraging further discussion or a meeting.
Use clear and natural language, avoid generic phrases, and personalize the proposal based on the project details.
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