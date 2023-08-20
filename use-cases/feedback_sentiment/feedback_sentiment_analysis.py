import os
import pandas as pd
from genai.credentials import Credentials
from genai.schemas import GenerateParams
from genai.model import Model
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GENAI_KEY", None)
api_url = os.getenv("GENAI_API", None)

creds = Credentials(api_key=api_key, api_endpoint=api_url)
params = GenerateParams(decoding_method="greedy", min_new_tokens=1, max_new_tokens=10)
model = Model("bigcode/starcoder", params=params, credentials=creds)

def getSoemthing():
    return "something"


def getImprovements(str):
    df = pd.read_csv("../assets/session_feedback.csv")
    #df = pd.read_csv("../../assets/session_feedback_10.csv")

    feedback_list = df["Feedback"].tolist()
    sentiment_array = []

    for feedback in feedback_list:
        prompt = f"""Classify this review as positive or negative. 
        Review: 
        {feedback}
        """
        result = model.generate([prompt])    
        sentiment_array.append(result[0].generated_text)

    df.insert(1, "Sentiment", sentiment_array, True)
    df_negative =  df[df["Sentiment"] == "negative"]
    response  = df_negative["Feedback"].tolist() 

    return response
