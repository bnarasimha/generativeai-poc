import os
from dotenv import load_dotenv
from genai.credentials import Credentials
from genai.model import Model
from genai.schemas import GenerateParams, ModelType

load_dotenv()
api_key = 'pak-AxfXuCD-pojaKDBneLyRXXiNNlJVkb-Cc1PyU9rxwJk' #os.getenv("GENAI_KEY", None)
api_url = 'https://bam-api.res.ibm.com/v1/' #os.getenv("GENAI_API", None)

creds = Credentials(api_key, api_endpoint=api_url) # credentials object to access the LLM service

# Instantiate parameters for text generation
params = GenerateParams(decoding_method="greedy", max_new_tokens=50)
model = Model("bigcode/starcoder", params=params, credentials=creds)

text = """
Write a simple poem on coding.
"""




response = model.generate([text])
res_sentence = response[0].generated_text

print(res_sentence)


