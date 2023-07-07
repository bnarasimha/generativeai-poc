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

print(get_completion(prompt))