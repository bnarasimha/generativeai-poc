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
Agent: Okay, I am awaiting your instructions

User: Watson, here are your instructions:
1. You will be given a document that should be used to reply to user questions.
2. You should generate the next response using information available in the document.
3. If you can't find an answer, say "I don't know".
4. Your responses should not be long and just have about 1-2 sentences.
5. You should not repeat your answers.
6. Do not use any other knowledge.

Please repeat the instructions back to me so that I know you understood.

Agent: Ok, here are my instructions:
1. I will be given a document that should be used to reply to user questions.
2. I should generate the next response using information available in the document.
3. If you can't find an answer, say "I don't know".
4. My responses should not be long and just have about 1-2 sentences.
5. I should not repeat your answers.
6. I will not use any other knowledge.

I am ready, please give me the document.

User: Here's the document: {

Timeline and Deadlines
Link to this section

Question: Is there an official deadline for migrating all z/OS repositories to the CI/CD pipeline? What will happen if I can't migrate my application by the deadline set by ITSS?

Answer: According to ITSS Chapter 5, the official deadline for the migration is the end of June. However, it's important to note that GitHub has been a requirement for some time, with a temporary exception granted due to the Lift and Shift requirements. If your application cannot be migrated by the end of June, you will need to follow the process for a Risk as documented by the BISO organization. This process will include submitting a plan for migration and addressing the risk associated with not meeting the deadline.

Question: When will the CI/CD pipeline be production-ready for z/OS?

Answer: The CI/CD pipeline is already operational in production for some applications.

Sunset
Link to this section

Question: Considering legacy applications on a sunset path that undergo minimal changes, is there a significant benefit to migrating the code to CIO CI/CD given the amount of work involved?

Answer: If the application is scheduled for sunset this year, the only requirement is to archive the final code in GitHub. It's not necessary to focus on organizing the code extensively in GitHub; simply placing the contents in folders based on type is sufficient, without worrying about the number of files in each folder.

However, if the application is not sunset-bound this year, it must meet ITSS requirements. ITSS mandates that source code be stored in GitHub and comply with secure build processes, build signing, and other auditing requirements. Moving to the CI/CD pipeline satisfies ITSS requirements. While migrating does involve work, it brings benefits such as onboarding into ADDI, which provides improved visibility into the application. Additionally, all applications must be moved into Cirrus 2.0 within the next two years. Managing custom-built LPARs becomes impractical, and onboarding into the pipeline is necessary to transition to Cirrus 2.0.

Tools and Infrastructure
Link to this section

Question: Who is responsible for installing and maintaining the required tools, such as Python, zoau, wheelhouse, Git, DBB, on the z/OS server? Is it the responsibility of the z/OS team or the Applications teams?

Answer: We are working with the infrastructure team to establish a process where they will be responsible for installing and maintaining the required base tools. If these tools are not present on your z/OS system, you will need to create a ticket with the support team to have them installed. The objective is to have infrastructure team keeping these tools up to date as part of their standard maintenance process. We do not want the application teams to be burdened with this task. Additionally, we aim to have a single version of each tool on the systems to avoid multiple versions and ensure that the right tools are present on the appropriate systems. The documentation will be updated to include the instructions.

Question: Is it true that installing tools like Python, zoau, wheelhouse, Git, DBB by the Applications teams is out of compliance?

Answer: No, that information is not true. If the application teams install these tools as part of the pipeline, it is within compliance. However, it is important to ensure that the installed tools are kept up to date with patches. To reduce the workload on the application teams, we encourage the infrastructure team to handle the installation and maintenance of these tools. The applications are not considered out of compliance.

Question: Is the infrastructure available on the z/OS Legacy systems?

Answer: Yes, the infrastructure is available on the z/OS Legacy systems. However, if you are already using the pipeline, it is necessary to migrate to a Cirrus 2.0 system.

Question: In an environment with multiple applications, would each application need to perform its own installation on the z/OS side, or can they share the same structure?

Answer: Once the infrastructure team handles the installation, it will be done in one location that all teams can utilize. Therefore, there is no need for each application to perform separate installations.

Question: When using IDz or any other IDE, will the same set of tools installed for the development CI/CD pipeline be used? Are there any special setup requirements, considering that we will be using our personal user ID which may not have the tools installed under it?

Answer: Both IDz and VS Code with the Z Open Editor utilize the existing tools. You will need to ensure that your configuration points to the correct location. Since the tools will be installed and accessible to all users, there is no need to be concerned about your personal user ID using them.

Question: We have multiple applications in our libraries and use SCLM. Will we need to create a separate repository for each application?

Answer: Yes, you will need to separate the applications into individual repositories. If you have shared includes, it would be beneficial to separate them into their own repositories, owned by the appropriate team, while still being usable by other application teams as part of the build process.

Question: Is local compilation on IDz (e.g., PL/I code) supported?

Answer: Local actual compilation has not been supported in IDz for some time. Instead, IDz provides a user build function that copies the source to the host and compiles it using the true z/OS compiler.

Question: In our SCLM setup, we use multiple streams to manage different priority projects and utilize multiple test environments. What is the equivalent of this in Git?

Answer: In Git, branches are used to handle multiple changes. Git provides greater flexibility in managing differences and improved merge capabilities compared to SCLM. However, it's important to note that if multiple users change the same line of code, a merge conflict will still occur and need to be resolved.

Question: Can we have two test environments between the development and production environments (e.g., DEV -> Test -> Business Test -> Prod)?

Answer: Yes, you can have as many environments as needed. In Cirrus 2.0, the system is designed to accommodate up to four levels of environments easily. If additional environments are required, automation can be implemented to create them.

Question: How can we use IDz in the CI/CD Cirrus 2.0 for our IMS-based project?

Answer: You should be able to use IDz in your current environment. If you encounter any issues with a specific LPAR, please let us know in the Slack Channel, and we will coordinate with the infrastructure team to address it. While there may be some additional time required for the lift and shift process, our goal is to ensure that teams can be as productive as possible.

Git and GitHub
Link to this section

Question: What does the term "branch" mean in Git?

Answer: In Git, a branch refers to a logical version of a set of files. When you clone or pull a repository, you retrieve the entire repository, including all branches. (There are ways to limit this, but in the simplest and most common case, you get all branches.) All branches will be available in your local copy. However, it's important to note that Git does not recommend creating branches to represent traditional levels or environments. Branching models can vary, and for more information, we suggest referring to resources like this: https://www.atlassian.com/git/tutorials/using-branches

Question: We have multiple projects supporting one application with different delivery dates and multiple stages (e.g., dev, test). How do we go about with this kind of setup?

Answer: Working with Git makes it easier to track multiple projects simultaneously with different changes, but the process is different when using branches. We recommend reading more about branching models and their implications for managing multiple projects: https://www.atlassian.com/git/tutorials/using-branches

Question: Why is an encrypted key needed when we can connect z/OS and GitHub using an SSH public key?

Answer: The encrypted private key used for the SSH connection needs to be stored in the GitHub repository. If an unencrypted version were used, anyone with read access to the GitHub repo would be able to make changes to your environments. Encryption adds an extra layer of security to protect sensitive information.

Question: Can GitHub be integrated with change management tools like Jira?

Answer: Yes, GitHub offers integrations with various tools, including Jira. You can explore the available GitHub Enterprise integrations specific to IBM here: https://w3.ibm.com/#/support/article/github_ent_ibm/github_migrate?_lang=en

For information on Jira integrations, you can refer to this resource: https://w3.ibm.com/#/support/article/jira_at_ibm

Additionally, the GitHub documentation provides guidance on connecting a GitHub Enterprise Server account to Jira Software: https://support.atlassian.com/jira-cloud-administration/docs/connect-a-github-enterprise-server-account-to-jira-software/

Supported Languages and Middleware
Link to this section

Question: Is the Rexx language included in the CI/CD pipeline? How will it be handled?

Answer: Yes, Rexx is supported in the CI/CD pipeline. Both Interpreted Rexx and compiled Rexx can be handled in the pipeline. Basic configuration is required for all languages in the pipeline, including Rexx. However, it is not complicated and is part of the initial setup process.

Question: Is CI/CD ready to work with IMS applications?

Answer: There are no restrictions on the old LPARs for what is supported in the pipeline. For legacy LPARs or redeploy LPARs, the full deployment process is not being replaced or automated due to their variations. The existing deployment process will be utilized, and the pipeline will handle the movement of load modules and bindings. If there are additional REXX or other automation for deployment, they can be integrated into the pipeline. Work is being done to support new world IMS deployment in Cirrus 2.0.

Question: How will the pipeline support middleware upgrades?

Answer: In Cirrus 2.0, there are multiple levels of pipelines. From an application perspective, the application pipeline will be responsible for making the appropriate middleware updates specific to the application. However, it will not upgrade the middleware itself. The application pipeline can target an updated version of the middleware, but the actual upgrades of middleware and operating system changes will be handled by the infrastructure pipeline.

Developer Tasks and Processes
Link to this section

Question: Can we re-run a specific failed step of the pipeline and resume from there?

Answer: The pipeline is designed for users to compile and test their code using User Build first. Failures in the pipeline are typically related to failed tests, which need to be fixed before rerunning the pipeline. Currently, the pipeline is relatively quick due to limited automated testing. As testing increases, it will be beneficial to address all failed tests together to improve efficiency.

Question: Do developers need to individually clone the repository and install applications in z/OS?

Answer: There are two aspects to consider: the migration into the pipeline and the day-to-day activities. When it comes to the migration into the pipeline, tools on z/OS need to be installed, and this task can be performed by one of the developers. However, for day-to-day activities, each developer simply needs to clone the Git repository locally and set up their preferred IDE.

Question: How can we back out a change? Do we need to rebuild and redeploy to override the last change?

Answer: Backing out a change may be necessary in some cases, and the backout process needs to be defined in collaboration with the teams. Wazi Deploy can create a backout package that allows rolling back to the state before the change. However, it is generally better to roll forward by making a new change and pushing it through the pipeline. This approach becomes preferable as teams adopt more automated testing. In the pipeline, building is not necessary beyond the development environment. The release pipeline is used to deploy an already built package to the respective environments.

Question: My application has the development environment on one LPAR and Production on another LPAR. In that case, do I need to configure CI/CD twice? In both DEV and PROD servers? How does deployment from DEV to PROD work?

Answer: Configuration of the process is done within the repository. You will have build.yml and multiple deploy.yml files to define the expected runtime environments. The build-related tools should be set up in the development environment. The pipeline will build the required artifacts, store the package in the artifact repository, and deploy them to the defined development environment. There is a secondary pipeline used for deploying to later stages, which utilizes the artifacts created by the initial build. It deploys the artifacts to subsequent test and production environments. If any issues arise, you can go back to the initial pipeline to create a new package.

Please refer to the documentation for more details: https://pages.github.ibm.com/cio-ci-cd/documentation/zos/concepts/workflow/

Deployment-related tools will indeed need to be present in the later stage environments. Our collaboration with the infrastructure team ensures that the appropriate tools are available in the respective environments.
}

Agent: I am ready to answer your questions from the document. I will not repeat answers I have given.

User:  Do devlopers have to individually clone repos?
Agent: 
"""


few_shot_prompt_examples  = """
Topic:
timely education session - the speakers seemed knowledgeable about the new world
Everything
The Q&A section
QA
Clear walk through of how to implement CI/CD pipeline. I really liked to documentation being updated

Summary:    xyz



Topic:
timely education session - the speakers seemed knowledgeable about the new world
Everything
The Q&A section
QA
Clear walk through of how to implement CI/CD pipeline. I really liked to documentation being updated

Summary:    a





"""

question = f"""Is there an official deadline for migrating all z/OS repositories to the CI/CD pipeline?"""

prompt = """
Summarize the below responses from participants:.

{few_shot_prompt_examples}

Topic: 

Summary:

"""

response = model.generate([prompt])
res_sentence = response[0].generated_text

print(res_sentence)


