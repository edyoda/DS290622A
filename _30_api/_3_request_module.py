import requests

url = "https://mocki.io/v1/d4867d8b-b5d5-4a48-a4ab-79131b5809b8"

response = requests.get(url).json()
# print(response.status_code)
print(response)

print(type(response))

print(response[-1]['city'])

print(response[3]["city"])


