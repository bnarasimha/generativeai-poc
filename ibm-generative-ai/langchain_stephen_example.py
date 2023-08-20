from langchain.document_loaders import PyPDFDirectoryLoader
from langchain.chains.question_answering import load_qa_chain
from genai.model import Credentials
from genai.schemas import GenerateParams
from genai.extensions.langchain.llm import LangChainInterface
from dotenv import load_dotenv
from os import environ


load_dotenv()

loader = PyPDFDirectoryLoader('../assets/.')
documents = loader.load_and_split()

model_id = 'google/flan-ul2'
params = GenerateParams(
    decoding_method='greedy',
    repetition_penalty=1.0,
    min_new_tokens=1,
    max_new_tokens=100
)

credentials = Credentials(environ['GENAI_KEY'], api_endpoint=environ['GENAI_API'])
llm = LangChainInterface(credentials=credentials, model=model_id, params=params)

while True:
    query = input('>> ')
    if query in ['exit']:
        break

    chain = load_qa_chain(llm, chain_type='stuff')
    print(chain.run(input_documents=documents[0:14], question=query))