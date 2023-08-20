from ibm_watson_machine_learning.foundation_models import Model
from ibm_watson_machine_learning.metanames import GenTextParamsMetaNames as GenParams
from ibm_watson_machine_learning.foundation_models.utils.enums import ModelTypes, DecodingMethods

# To display example params enter
GenParams().get_example_values()

generate_params = {
    GenParams.MAX_NEW_TOKENS: 25
}

creds = {
        "apikey": "530OW4n6xUss3mtaPzCxVpEgVryJegIQx87yNukS9W75",
        "url": "https://us-south.ml.cloud.ibm.com"
    }

model = Model(
    model_id=ModelTypes.FLAN_UL2,
    params=generate_params,
    credentials=creds,
    project_id="0712ea07-18f3-4fd4-807d-c874ac6fa351"
    )

loader = PyPDFDirectoryLoader('.')
documents = loader.load_and_split()

llm = LangChainInterface(credentials=credentials, model=model_id, params=params)

q = "What is 1 + 1?"
generated_response = model.generate(prompt=q)
print(generated_response['results'][0]['generated_text'])