lst = [7,4,89,100,38,5,4,2,2]
num = int(input("Enter a value to check whether it is present within the list or not : "))

if num in lst or num > 10:
    print("It is present!")
else:
    print("It is not present!")