import os
from dotenv import load_dotenv
load_dotenv()

import os
import requests

api_key = os.environ.get("OPENROUTER_API_KEY")
headers = {
    'Authorization': f'Bearer {api_key}',
    'Content-Type': 'application/json'
}
payload = {
    'model': 'openrouter/free',
    'messages': [{'role': 'user', 'content': 'Hello!'}]
}

resp = requests.post('https://openrouter.ai/api/v1/chat/completions', json=payload, headers=headers)
print(resp.json())
