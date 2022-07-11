age = int(input("Enter age : "))

if age >= 18:
    print(f"Your age is {age}, hence you are eligible to work with us!")
    qualification = int(input("But we will first have to know your qualification. Please mention it : "))
    if qualification > 12:
        print("Yes, you are hired. Congrats!!!")
    else:
        print("Sorry we would like to consider another candidate!!!")
else:
    print("You are too young to work with us!")