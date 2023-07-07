import os
import openai

openai.api_key  = os.environ['OPENAI_API_KEY']

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, 
    )
    return response.choices[0].message["content"]


text = """
Write a simple poem on coding.
"""


prompt = f""" what is the revene delivered in financial highlights provided \
that is delimited by triple backticks
financial highlights: ```{text}```
"""

print(get_completion(text))