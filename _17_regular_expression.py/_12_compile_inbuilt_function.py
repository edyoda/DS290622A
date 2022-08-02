import re

password = input("Enter an password : ")
result = re.compile(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!#%*?&]{8,16}$")
res = result.search(password)
print(res)
if res:
    print("Password is correct")
else:
    print("Password is incorrect")