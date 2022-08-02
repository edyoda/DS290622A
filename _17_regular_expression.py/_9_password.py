import re
password = input("Enter an password : ")
result = re.search(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!#%*?&]{8,16}$",password)#[A-Za-z0-9@#$%^&+=_.]{8,16}$",password)

if result:
    print("Password is correct")
else:
    print("Password is incorrect")



