# Evaluate api testing

This is sample repo to demo the evaulate API with Azure Machine Learning Studio and some of the issues I have come across. To keep it simple, it does not use any LLM calls and the flow response is hardcoded.

## Getting started

Before running, there must be an AML Workspace and App Insights deployed

1. Optionally open in devcontainer -> Use the Dev Containers: Open Workspace in Container... command.
2. Install requirements ->  `pip install -r requirements.txt`
3. Log in to az CLI -> `az login` 
4. Copy and fill out .env file. -> `cp sample.env .env` -> fill in values
5. Run the evaluate script -> `python ./evaluate.py`


## Issues

1. I am not able to get trace to App Insights using the connection string. Is there another way?
2. Creating a custom span does not show up in the AML workspace UI but it is available in the local tracing experience
