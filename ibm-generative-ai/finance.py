import os
from dotenv import load_dotenv
from genai.credentials import Credentials
from genai.model import Model
from genai.schemas import GenerateParams, ModelType

load_dotenv()
api_key = os.getenv("GENAI_KEY", None)
api_url = "https://us-south.ml.cloud.ibm.com/ml/v1-beta/generation/text?version=2023-05-29"#os.getenv("GENAI_API", None)

creds = Credentials(api_key, api_endpoint=api_url) # credentials object to access the LLM service

# Instantiate parameters for text generation
params = GenerateParams(decoding_method="greedy", max_new_tokens=50)
model = Model("bigscience/bloom", params=params, credentials=creds)

text = """
Financial Highlights
Thanks Arvind. I’ll start with the financial highlights of the fourth quarter. We delivered $16.7 billion in revenue, $3.8 billion of operating pre-tax income and operating earnings per share of $3.60. In our seasonally strongest quarter, we generated $5.2 billion of free cash flow. Our revenue for the quarter was up over six percent at constant currency. While the dollar weakened a bit from 90 days ago, it still impacted our reported revenue by over $1 billion – and 6.3 points of growth. As always, I’ll focus my comments on constant currency. And I’ll remind you that we wrapped on the separation of Kyndryl at the beginning of November. The one-month contribution to our fourth quarter revenue growth was offset by the impact of our divested health business.
Revenue growth this quarter was again broad based. Software revenue was up eight percent and Consulting up nine percent. These are our growth vectors and represent over 70 percent of our revenue. Infrastructure was up seven percent. Within each of these segments, our growth was pervasive. We also had good growth across our geographies, with mid-single digit growth or better in Americas, EMEA and Asia Pacific. And for the year, we gained share overall. We had strong transactional growth in software and hardware to close the year. At the same time, our recurring revenue, which provides a solid base of revenue and profit, also grew – led by software. I’ll remind you that on an annual basis, about half of our revenue is recurring.
Over the last year, we’ve seen the results of a more focused hybrid cloud and AI strategy. Our approach to hybrid cloud is platform centric. As we land the platform, we get a multiplier effect across Software, Consulting and Infrastructure. For the year, our hybrid cloud revenue was over $22 IBM 4Q22 Earnings Prepared Remarks billion – up 17 percent from 2021.
Looking at our profit metrics for the quarter, we expanded operating pretax margin by 170 basis points. This reflects a strong portfolio mix and improving Software and Consulting margins. These same dynamics drove a 60-basis point increase in operating gross margin. Our expense was down year to year, driven by currency dynamics. Within our base expense, the work we’re doing to digitally transform our operations provides flexibility to continue to invest in innovation and in talent. Our operating tax rate was 14 percent, which is flat versus last year. And our operating earnings per share of $3.60 was up over seven percent. Turning to free cash flow, we generated $5.2 billion in the quarter and $9.3 billion for the year. Our full-year free cash flow is up $2.8 billion from 2021. As we talked about all year, we have a few drivers of our free cash flow growth. First, I’ll remind you 2021’s cash flow results included Kyndryl-related activity – including the impact of spin charges and capex. Second, we had working capital improvements driven by efficiencies in our collections and mainframe cycle dynamics. Despite strong collections, the combination of revenue performance above our model and the timing of the transactions in the quarter led to higher-than-expected working capital at the end of the year. This impacted our free cash flow performance versus expectations. Our year-to-year free cash flow growth also includes a modest tailwind from cash tax payments and lower payments for structural actions, partially offset by increased capex investment for today’s IBM.
In terms of cash uses for the year, we invested $2.3 billion dollars to acquire eight companies across software and consulting, mitigated by over a billion dollars in proceeds from divested businesses, and we returned nearly six billion dollars to shareholders in the form of dividends. From a  IBM 4Q22 Earnings Prepared Remarks balance sheet perspective, we ended the year in a strong liquidity position with cash of $8.8 billion. This is up over a billion dollars year to year. And our debt balance is down nearly a billion dollars. Our balance sheet remains strong, and I’d say the same for our retirement-related plans. At year end, our worldwide tax-qualified plans are funded at 114 percent, with the U.S. at 125 percent. Both are up year to year. You’ll recall back in September, we took another step to reduce the risk profile of our plans. We transferred a portion of our U.S. qualified defined benefit plan obligations to insurers, without changing the benefits payable to plan participants. This resulted in a significant non-cash charge in our GAAP results in the third quarter, and we’ll see a benefit in our nonoperating charges going forward. You can see the benefit of this and other pension assumptions to the 2023 retirement-related costs in our supplemental charts.
"""


prompt = f""" what is the revenue delivered in the below financial highlights \
delimited by triple backticks
financial highlights: ```{text}```
"""

response = model.generate([prompt])
res_sentence = response[0].generated_text

print(res_sentence)


