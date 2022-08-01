# import re
# pincode = input("Enter your pincode : ")

# res = re.findall("^[1-9]{1}[0-9]{5}$",pincode)

# if res:
#     print("Format is correct")
# else:
#     print("Format is incorrect")






str1 = "Hey you/ all\\"
data = str1.split("/")
str1 = "".join(data)
print(str1)