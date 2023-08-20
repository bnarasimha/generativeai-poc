import os
from dotenv import load_dotenv
from genai.credentials import Credentials
from genai.model import Model
from genai.schemas import GenerateParams
from genai.prompt_pattern import PromptPattern


load_dotenv()
api_key = os.getenv("GENAI_KEY", None)
api_url = os.getenv("GENAI_API", None)

creds = Credentials(api_key, api_endpoint=api_url) # credentials object to access the LLM service

# Instantiate parameters for text generation
params = GenerateParams(decoding_method="greedy", min_new_tokens=50, max_new_tokens=200)
model = Model("google/flan-ul2", params=params, credentials=creds)


_path_to_template_file = "../assets/synth-animal.yaml"
_path_to_csv_file = "../assets/penguins.csv"
# Create prompt pattern from the file
prompt = PromptPattern.from_file(_path_to_template_file)
mapping = {
    "species": ["species1", "species2", "species3"],
    "island": ["location1", "location2", "location3"],
    "year": ["dob1", "dob2", "dob3"],
}

list_of_prompts = prompt.sub_all_from_csv(
    csv_path=_path_to_csv_file,
    col_to_var=mapping,
)

print("-----------------------")
print("generated prompt")
print(list_of_prompts)
print(len(list_of_prompts))
print("-----------------------")


responses = model.generate_as_completed(list_of_prompts)
for response in responses:
    print(f"Generated text: {response.generated_text}")