import requests
import json

URL = "http://127.0.0.1:8000/stupost/"

# Python Object which we can't send to server (That's why convert into json)
data = {
    'name': 'Umair',
    'roll': 0o04,
    'city': 'foolish'
}

# Convert Python Object to Json by using dump() method
json_data = json.dumps(data)
print("Json Data" + json_data)
response = requests.post(url=URL, data=json_data)
print(data)
