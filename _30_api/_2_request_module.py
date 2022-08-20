# http://ip.jsontest.com/

import requests

url = "http://ip.jsontest.com/"

response = requests.request('GET',url).json()
print(response)

print(type(response))

print(response["ip"])