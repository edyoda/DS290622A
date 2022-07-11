num = int(input("Enter a value to check if it +ve value or -ve value : "))

if num > 0:
    print(f"{num} is a +ve number!")
elif num == 0:
    print(f"{num} is neutral!")
else:
    print(f"{num} is a -ve number!")