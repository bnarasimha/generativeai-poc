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
params = GenerateParams(decoding_method="greedy", min_new_tokens=100, max_new_tokens=150)
model = Model("bigscience/bloom", params=params, credentials=creds)

def getFeedbackSummary(filePath):
    df = pd.read_csv("../../assets/sample_feedback.csv")
    text_to_summarize = df["Feedback"].tolist()

    prompt = """Summarize the following responses: 
    {text_to_summarize}
    """

    response = model.generate(prompt)
    return response[0].generated_text