import requests
import app

API_BASE_URL = "https://api.cloudflare.com/client/v4/accounts/d40839592c82f678e6a1eccbefc3e985/ai/run/"
headers = {"Authorization": "Bearer 9IvrVFhROkcjUWWGdpG8TstRfEm09J0ANETqQrBY"}

def run(model, inputs):
    input = { "messages": inputs }
    response = requests.post(f"{API_BASE_URL}{model}", headers=headers, json=input)
    full_result = response.json()
    response_only = full_result.get('result', {}).get('response', '')
    return response_only

# get string of skills from resume
condensed = "my skills are "

def getfile(file) :
    skill_list = app.extract_skills_from_resume()
    for item in skill_list :
        condensed += item
        condensed += " "

# interview questions
inputs = [
    { "role": "system", "content": "You are an assistant that helps provide interview questions" },
    { "role": "user", "content": condensed}
]

output = run("@cf/meta/llama-2-7b-chat-int8", inputs)
print(output) 

# answers provided by user
answers = [ 
    { "role": "system", "content": "You are an assistant that provides constructive critism on the interview answers given and if they're good answers" },
    { "role": "user", "content": "I worked on a python verison of the pokemon game. IT was really hard and I don't derserve this position."}
]

output = run("@cf/meta/llama-2-7b-chat-int8", answers)
print(output) 