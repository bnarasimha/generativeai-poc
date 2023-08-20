import os

from dotenv import load_dotenv

try:
    from langchain import PromptTemplate
    from langchain.chains import LLMChain, SimpleSequentialChain, RetrievalQA
    from langchain.embeddings.openai import OpenAIEmbeddings
    from langchain.vectorstores import Chroma
    from langchain.text_splitter import CharacterTextSplitter
    from langchain.chains import RetrievalQA
    from langchain.document_loaders import TextLoader
except ImportError:
    raise ImportError("Could not import langchain: Please install ibm-generative-ai[langchain] extension.")

from genai.extensions.langchain import LangChainInterface
from genai.model import Credentials
from genai.schemas import GenerateParams, ModelType

# make sure you have a .env file under genai root with
# GENAI_KEY=<your-genai-key>
load_dotenv()
api_key = os.getenv("GENAI_KEY", None)
api_url = os.getenv("GENAI_API", None)
open_ai_key = os.getenv("OPEN_AI_KEY", None)


creds = Credentials(api_key, api_endpoint=api_url)
model = LangChainInterface(model=ModelType.FLAN_UL2, credentials=creds)


loader = TextLoader("/Users/veroniquedemers/git/genai/bampy/examples/user/assets/state_of_the_union.txt")
documents = loader.load()
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
texts = text_splitter.split_documents(documents)

embeddings = OpenAIEmbeddings(openai_api_key=open_ai_key)
docsearch = Chroma.from_documents(texts, embeddings)


qa = RetrievalQA.from_chain_type(
    llm=model,
    chain_type="stuff",
    retriever=docsearch.as_retriever())

query = "What did the president say about Ketanji Brown Jackson"
a = qa.run(query)
print(a)