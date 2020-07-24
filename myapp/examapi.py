import json

import requests

url = 'https://opentdb.com/api.php?amount=10&category=9&difficulty=easy&type=multiple'
response = requests.get(url)
document = json.loads(response.text)
print(document)