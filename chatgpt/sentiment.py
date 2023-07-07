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
For me was not expected. I was hoping that give us the how move our code with a clear example
this topic is very foreign to many of us ... and questions like what would you like to see as far as tools ... means nothing to us - we have not used any of it and barely understand on how we have to translate what we currently do to the new world.  I am thinking of breaking it down even more.  I was so excited when I saw the first presenter talk about jcl and showed jcl ... but then they lost me - today if I need to update a dsn in jcl, I go into the editor update it done and can run immediately and tell if I have a typo or not.  How does that work in the new world ... looks like it would take several steps before even being able to test to see if I had a typo ... it would of helped me to see the jcl go all the way through the process from update to running the jcl.  I understand the general concepts ... but how to convert what I do today to tomorrow ... not getting the picture.

Keep up the good work

ensure that the presenters are more familiar with the material and that the material addresses z/OS
It will be good if the links to the previous events are also there.
more topics like this

Links to documentation etc to be added so we can go to it from the presentation.
"""

prompt = """
What is the sentiment of the below feedback:
{text}
""" 

print(get_completion(text))