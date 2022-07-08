"""
Logical Operators - it returns bool value

and - it will return True only if all the mentioned conditions are True
or  - it will return True if atleast one condition is True
not - it returns the reverse of the actual result
"""

num1 = int(input("Enter your first number : "))
num2 = int(input("Enter your second number : "))
num3 = int(input("Enter your third number : "))

and_demo = num1 == num2 and num1 > num3 
print("And : ",and_demo)

or_demo = num1 == num2 or num1 > num3 
print("Or : ",or_demo)

not_demo = not(num1 == num2 and num1 > num3)
print("Not : ",not_demo)




