import os
from dotenv import load_dotenv
load_dotenv()

import requests
import os

api_key = os.environ.get("GROQ_API_KEY")
url = "https://api.groq.com/openai/v1/models"
headers = {"Authorization": f"Bearer {api_key}"}

res = requests.get(url, headers=headers)
if res.status_code == 200:
    models = res.json().get("data", [])
    for m in models:
        print(m["id"])
else:
    print(res.status_code, res.text)
