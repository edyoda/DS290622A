# it is used to check multiple conditions

from tkinter import N


num1 = int(input("Enter 1st value : "))
num2 = int(input("Enter 2nd value : "))

if num1 > num2:
    print("num1 is greater than num2")
elif num1 == num2:
    print("num1 is equal to num2")
else:
    print("num2 is greater than num1")