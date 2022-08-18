import json

json_obj = """{
    "rno":1,
    "name":"Bharati",
    "address":"Mumbai",
    "female":true,
    "qualification":null
}"""

# return json object as a dict object
dict_obj = json.loads(json_obj)

print(dict_obj)
print(type(dict_obj))

# returns dict object as a json object
json_obj = json.dumps(dict_obj)
print(json_obj)