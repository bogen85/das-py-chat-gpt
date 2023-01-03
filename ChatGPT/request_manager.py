import requests
from pprint import pprint

def send_message(model_id, api_key, message):
    # Send message to ChatGPT API and get response
    response = requests.post(
        "https://api.openai.com/v1/completions",
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        },
        json={
            "model": model_id,
            "prompt": message,
            "max_tokens": 3900,
            "temperature": 0.5,
            "top_p": 1,
            "stream" : False,
            "frequency_penalty": 0,
            "presence_penalty": 0
        }
    )
    response_json = response.json()
    pprint(response_json)
    response_text = response_json['choices'][0]['text']
    return response_text
