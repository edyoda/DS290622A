import re
password = input("Enter an e-mail: ")
result = re.findall(r"^(.*[a-z])(.*[A-Z])(.*[0-9])(.*[@#$%^&+=_.])[A-Za-z0-9@#$%^&+=_.]$",password)#[A-Za-z0-9@#$%^&+=_.]{8,16}$",password)

if result:
    print("Email is correct")
else:
    print("Email is incorrect")


# order and size is pending

