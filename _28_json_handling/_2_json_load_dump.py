import json

file = open("B:\DS290622A\DS290622A\_28_json_handling\json_dump.json")

# return the json object as a dictionary object
data = json.load(file)
print(data)
print(type(data))


file1 = open("B:\DS290622A\DS290622A\_28_json_handling\json_dump1.json","w")

# return the dict object as a jsob object
json.dump(data,file1)