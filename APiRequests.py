import requests

response = requests.get("https://api.github.com")

print(response.status_code)

data = {"name": "John"}

response = requests.post("https://httpbin.org/post", data=data)
print(response.json())