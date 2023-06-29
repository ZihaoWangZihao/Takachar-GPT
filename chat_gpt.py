import openai
import requests
from api_key import *
from pdf_scrape import *

headers = {
    'Content-Type': 'application/json',
    'Authorization': f"Bearer {api_key}"
}

def gpt(role, question):
    """
    :param role: <str> - role gpt takes on
    :param question: <str> - question you ask gpt
    :return: <str> - gpt response
    """
    data = {
        'messages': [
            {'role': 'system', 'content': role},
            {'role': 'user', 'content': question}
        ],
        'model': 'gpt-3.5-turbo'
    }

    api_url = 'https://api.openai.com/v1/chat/completions'
    response = requests.post(api_url, headers=headers, json=data)

    if response.status_code == 200:
        response_data = response.json()
        reply = response_data['choices'][0]['message']['content']
        return reply
    else:
        message = 'Error:', response.status_code, response.text
        return message

role = "You are a data science employee working for Takachar."
question = f"Given the following hot tests, find me the date that hot test 2 occured on: {extracted_text}"
print(gpt(role, question))

