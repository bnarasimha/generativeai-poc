import os
import pandas as pd
from dotenv import load_dotenv
from genai.credentials import Credentials
from genai.model import Model
from genai.schemas import GenerateParams, ModelType

load_dotenv()
api_key = os.getenv("GENAI_KEY", None)
api_url = os.getenv("GENAI_API", None)

creds = Credentials(api_key,api_endpoint=api_url)

params = GenerateParams(decoding_method="greedy", min_new_tokens=10, max_new_tokens=100)
model = Model("google/flan-ul2", params=params, credentials=creds)

df =  pd.read_csv("../assets/DevAdv_SurveyRsults.csv")

text = df["Overall, how satisfied were you with the event?"]

#print(text)

prompt = """
You role is a data analyst.

Below is the list of responses received from participants from a seminar

Responses: ```{text}```, 
 
How many are Dissatisfied?"""

response = model.generate([prompt])
res_sentence = response[0].generated_text

print(res_sentence)
