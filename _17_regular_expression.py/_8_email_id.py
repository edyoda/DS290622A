import re
email = input("Enter an e-mail: ")
result = re.findall(r"[a-zA-Z0-9._]+[@][a-z+]+[.]{1}[a-z]+$",email)

if result:
    print("Email is correct")
else:
    print("Email is incorrect")
