from dotenv import load_dotenv 
import requests
import os

load_dotenv()

def query_llm(prompt):
    api_url = "YOUR_ENDPOINT"
    api_key = "YOUR_KEY"

    req_header = {
        "Authorization": f"Bearer {api_key}"
    }
    # For additional configuration, go to https://huggingface.co/docs/api-inference/detailed_parameters#text-generation-task
    req_body = {
        "inputs": prompt
    }
    response = requests.post(url=api_url, json=req_body, headers=req_header)

    return response.json()

# Additional information that LLM does not know
context = """
    Auryn is a gray, medium hair cat born in March, 2012. She is a maine coon mix who sports a medium sized mane and cute tufts on her ears and toes. She is clicker trained, and she can perform tricks such as sit, sit pretty, high five, high ten, and turn. She loves to eat, except when she is nervous. Her favorite food is chicken and pork. 
"""

# Question about the context that LLM wouldn't know otherwise
user_question = "What is Auryn's favorite food?"

#TODO
prompt = ""

print(query_llm(prompt))