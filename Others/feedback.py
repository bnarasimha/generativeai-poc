import os
import openai
import pandas as pd

openai.api_key  = os.environ['OPENAI_API_KEY']

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, 
    )
    return response.choices[0].message["content"]


file_name = "../assets/DevAdv_SurveyRsults.csv"
column_name = "Overall, how satisfied were you with the event?"

df = pd.read_csv(file_name)

text = df[column_name]
text_dict = df[column_name].to_list()
feedbackstr = ""

for feedback in text_dict:
    feedbackstr += feedback + "\n"

#print(feedbackstr)

prompt = f"""
You role is a data analyst.

Below is the list of responses received from participants from a seminar.

{feedbackstr}
 
How many are Satisfied?"""

print(get_completion(prompt))
#print(prompt)