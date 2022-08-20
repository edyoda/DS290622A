import requests
url = "http://api.zippopotam.us/us/90210"
response = requests.get(url).json()

print(response)

# https://www.w3schools.com/tags/ref_httpmethods.asp