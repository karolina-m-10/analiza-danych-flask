import requests

url = 'http://127.0.0.1:5000/predict'
data = {'x1': 6, 'x2': 7}

response = requests.post(url, json=data)

print("Status:", response.status_code)
print("Response:", response.json())
