import openai
import os
# Replace 'your-openai-api-key' with your actual OpenAI API key

openai.api_key  = os.environ['OPENAI_API_KEY']
#openai.api_key = 'your-openai-api-key'

# Prompt for the language model
prompt = "Once upon a time, there was a brave knight..."

# Number of responses to generate
num_responses = 5

# Generate responses using a for loop
for _ in range(num_responses):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        temperature=0.7,
        max_tokens=150,
        n=1,
        stop=None,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )

    generated_text = response['choices'][0]['text']
    print(f"Generated Response: {generated_text}\n")
