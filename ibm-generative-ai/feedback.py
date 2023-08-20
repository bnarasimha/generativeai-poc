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

params = GenerateParams(decoding_method="greedy", min_new_tokens=10, max_new_tokens=10)
model = Model("google/flan-ul2", params=params, credentials=creds)

df =  pd.read_csv("../assets/DevAdv_SurveyRsults.csv")

column_name = "Overall, how satisfied were you with the event?"
text = df[column_name]

text_dict = df[column_name].to_list()

feedbackstr = ""

for feedback in text_dict:
    feedbackstr += feedback + "\n"

prompt = f"""
I want you to act as a data scientist.

Below is the dataset of responses received from participants from a seminar:

Responses: {feedbackstr}

Answer the below question from the dataaset:
How many people responded as Dissatisfied?"""

response = model.generate([prompt])
res_sentence = response[0].generated_text

#print(prompt)
print(response[0].generated_text)