dict1 = {1:"Ram",2:"Laxman",3:"Sita"}
print("Original dict : ",dict1)

# data = dict1[4] # to fetch the value on bases of keys, but it raises error if it is not present
# print(data)

# data = dict1.get(4,False) # it will handle if the key is not present in the dict
# print(data)

# key = dict1.keys() # to fetch keys
# print(key)

# for i in key:
#     print(i)

# value = dict1.values() # to fetch values
# print(value)

# for i in value:
#     print(i)

# for i in dict1.keys():
#     print(i)

# for i in dict1.values():
#     print(i)

# item = dict1.items() # to retrieve keys and values both
# print(item)

# for k,v in dict1.items(): 
#     print(k,"----->",v)

# dict1.clear() # delete all the elements
# print(dict1)

# dict2 = dict1.copy() # create copy of dict
# print(dict2)

dict2 = dict(name="Bharati",address="Mumbai")
print(dict2)

# dict2.pop("name")
# print(dict2)

dict2["mobile_no"] = 1234567890
print(dict2)

dict2.update({"age":10})
print(dict2)