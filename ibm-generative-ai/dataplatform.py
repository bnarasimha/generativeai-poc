import os, getpass, wget, json
import requests
from ibm_cloud_sdk_core import IAMTokenManager
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator, BearerTokenAuthenticator
from pandas import read_csv

endpoint_url = "https://us-south.ml.cloud.ibm.com"

class Prompt:
    def __init__(self, access_token, project_id):
        self.access_token = access_token
        self.project_id = project_id

    def generate(self, input, model_id, parameters):
        wml_url = f"{endpoint_url}/ml/v1-beta/generation/text?version=2023-05-28"
        Headers = {
            "Authorization": "Bearer " + self.access_token,
            "Content-Type": "application/json",
            "Accept": "application/json"
        }
        data = {
            "model_id": model_id,
            "input": input,
            "parameters": parameters,
            "project_id": self.project_id
        }
        response = requests.post(wml_url, json=data, headers=Headers)
        if response.status_code == 200:
            return response.json()["results"][0]
        else:
            return response.text
        

access_token = IAMTokenManager(
    apikey = getpass.getpass("Please enter your WML api key (hit enter): "),
    url = "https://iam.cloud.ibm.com/identity/token"
).get_token()


try:
    project_id = os.environ["PROJECT_ID"]
except KeyError:
    project_id = input("Please enter your project_id (hit enter): ")

filename_test = 'data/contracts_summarization_test.csv'
filename_train = 'data/contracts_summarization_train.csv'

test_data = read_csv(filename_test)[["original_text", "reference_summary"]]
train_data = read_csv(filename_train)[["original_text", "reference_summary"]]


print(json.dumps(train_data[:1].values.tolist(), indent=2))


models_json = requests.get(endpoint_url + '/ml/v1-beta/foundation_model_specs?version=2022-08-01&limit=50',
                           headers={
                                    'Authorization': f'Bearer {access_token}',
                                    'Content-Type': 'application/json',
                                    'Accept': 'application/json'
                            }).json()
models_ids = [m['model_id'] for m in models_json['resources']]
print(models_ids)

model_id = "google/flan-ul2"

instruction =  "Generate a brief summary of this document:\n"

few_shot_input = []
few_shot_target = []
singleoutput= []

for i,tl in enumerate(test_data.values):
    if (i+1)%2==0:
        singleoutput.append(f"    document: {tl[0]}    summary:")
        few_shot_input.append("".join(singleoutput))
        few_shot_target.append(tl[1])
        singleoutput = []
    else:
        singleoutput.append(f"    document: {tl[0]}    summary: {tl[1]}")


print(json.dumps(print(few_shot_input[0]), indent=2))

parameters = {
         "decoding_method": "greedy",
         "min_new_tokens": 1,
         "max_new_tokens": 80
}

prompt = Prompt(access_token, project_id)

results = []

for inp in few_shot_input:
    results.append(prompt.generate(" ".join([instruction, inp]), model_id, parameters)['generated_text'])



