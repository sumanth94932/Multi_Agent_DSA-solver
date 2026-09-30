import requests

resp = requests.get('https://openrouter.ai/api/v1/models')
data = resp.json()['data']

free_models = []
for model in data:
    pricing = model.get('pricing', {})
    prompt = float(pricing.get('prompt', 1))
    completion = float(pricing.get('completion', 1))
    if prompt == 0 and completion == 0:
        free_models.append(model)

for m in free_models:
    print("-", m['id'])
