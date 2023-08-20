from langchain.document_loaders import PyPDFDirectoryLoader
from langchain.chains.question_answering import load_qa_chain
from genai.model import Credentials
from genai.schemas import GenerateParams
from genai.extensions.langchain.llm import LangChainInterface
from dotenv import load_dotenv
from os import environ

load_dotenv()

loader = PyPDFDirectoryLoader('assets/')
documents = loader.load_and_split()

print("Fetched " + str(len(documents)) + " documents")