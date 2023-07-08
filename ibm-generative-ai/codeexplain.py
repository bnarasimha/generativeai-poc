import os
from dotenv import load_dotenv
from genai.credentials import Credentials
from genai.model import Model
from genai.schemas import GenerateParams, ModelType

load_dotenv()
api_key = os.getenv("GENAI_KEY", None)
api_url = os.getenv("GENAI_API", None)

creds = Credentials(api_key, api_endpoint=api_url) # credentials object to access the LLM service

# Instantiate parameters for text generation
params = GenerateParams(decoding_method="greedy", max_new_tokens=50)
model = Model("bigcode/starcoder", params=params, credentials=creds)

text = """
# Python 3
def gcd(x, y):
    while y != 0:
        (x, y) = (y, x % y)
    return x
"""


prompt = f""" explain the code \
that is delimited by triple backticks
code: ```{text}```
"""

response = model.generate([prompt])
res_sentence = response[0].generated_text

print(res_sentence)


