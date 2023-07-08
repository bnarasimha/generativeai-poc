import os
from dotenv import load_dotenv
from genai.credentials import Credentials
from genai.model import Model
from genai.schemas import GenerateParams, ModelType

load_dotenv()
api_key = os.getenv("GENAI_KEY", None)
api_url = os.getenv("GENAI_API", None)

creds = Credentials(api_key, api_endpoint=api_url) # credentials object to access the LLM service

# Instantiate parameters for text generation
params = GenerateParams(decoding_method="greedy", min_new_tokens=50, max_new_tokens=200)
model = Model("google/flan-ul2", params=params, credentials=creds)

text = """
Piyush Nandan
  13:16
Hi Narsimha
GA


Narasimha Badrinath
:spiral_calendar_pad:  13:22
Hi Piyush
13:22
GA


Piyush Nandan
  13:22
Regarding Contrast,
Since we already have vulnerabilities list from mend and sonarqube through CIO CI/CD,
can you please help me to know how the vulnerabilities list of contrast will be different from mend and sonarqube?
or any other suggestions from you?


Narasimha Badrinath
:spiral_calendar_pad:  13:22
Mend find vulnerabilities from opensource libraries
13:23
Sonar does only static code analysis
13:23
Contrast monitors application when its in use and checks if any API calls has vulnerabilities and flags it (edited) 
13:23
Sonar and Mend cant do that
13:24
More in terms of securing your applications from API attacks etc


Piyush Nandan
  13:24
contrast comes user IAST,
mend and sonar comes under SAST,
can you please tell if it is correct understanding?


Narasimha Badrinath
:spiral_calendar_pad:  13:25
Contrast also has SAST, but we are using Sonar for that. So you are right. For now Contrast for IAST.


Piyush Nandan
  13:25
one more query,
contrast can be done only for feature branch, why not main branch?


Narasimha Badrinath
:spiral_calendar_pad:  13:25
Mend and Sonar checks static code only
13:25
So yes


Piyush Nandan
  13:26
ok thank you


Narasimha Badrinath
:spiral_calendar_pad:  13:26
No problem
"""


prompt = f""" Write a short summary for the meeting transcripts. \
Transcript: {text}
"""

response = model.generate([prompt])
res_sentence = response[0].generated_text

print(res_sentence)


