import requests
import pprint

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
    try:
        response_text = response_json['choices'][0]['text']
        del(response_json['choices'][0]['text'])
        return (response_text, pprint.pformat(response_json))
    except Exception as e:
        return (str(e), pprint.pformat(response))

# CudaText: lexer_file="Python"; tab_size=4; tab_spaces=Yes; newline=LF;
