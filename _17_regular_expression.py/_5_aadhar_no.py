import re
# aadhar_no = input("Enter your aadhar no. : ")

# # 1234-5676-7898
# res = re.findall("^[1-9]{1}[0-9]{3}[-][0-9]{4}[-][0-9]{4}$",aadhar_no)

# if res:
#     print("Format is correct")
# else:
#     print("Format is incorrect")

# 1234 5678 4890
ad_no = input("Enter your Adhar No:")
res = re.search("^[1-9]{1}[0-9]{3}\s[0-9]{4}\s[0-9]{4}$",ad_no)

if res:
     print("Format is correct")
else:
     print("Format is incorrect")




