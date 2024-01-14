from flask import Flask, request, jsonify
import requests
import random
import skills
import os
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)

API_BASE_URL = "https://api.cloudflare.com/client/v4/accounts/d40839592c82f678e6a1eccbefc3e985/ai/run/"
headers = {"Authorization": "Bearer "+os.getenv("API_KEY")}

def run(model, inputs):
    input = { "messages": inputs }
    response = requests.post(f"{API_BASE_URL}{model}", headers=headers, json=input)
    full_result = response.json()
    response_only = full_result.get('result', {}).get('response', '')
    return response_only

# get string of skills from resume
def getQuestions(skill_list) :
    condensed = "my skills are "
    for item in skill_list :
        condensed += item
        condensed += " "

    # interview questions
    inputs = [
        { "role": "system", "content": "You are an assistant that helps provide interview questions with max 200 words" },
        { "role": "user", "content": condensed}
    ]

    output = run("@cf/meta/llama-2-7b-chat-int8", inputs)
    return output

def getFeedback(user_input) :
    answers = [ 
        { "role": "system", "content": "You are an assistant that provides constructive critism on the interview answers given and if they're good answers with max 200 words" },
        { "role": "user", "content": user_input}
    ]

    output = run("@cf/meta/llama-2-7b-chat-int8", answers)
    return output

def getJoke():
    joke = [ 
        { "role": "system", "content": "Tell a joke" },
    ]

    output = run("@cf/meta/llama-2-7b-chat-int8", joke)
    return output
