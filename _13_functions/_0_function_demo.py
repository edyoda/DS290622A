# function

# it is use to reuse the code
# you can use the same set of code with little modification if needed
# Syntax : 
# def <function_name>():
#     function_body

# a function without return type and without any arguments
def addition():                          # defining the function
    no1 = int(input("Enter number1 : "))
    no2 = int(input("Enter number2 : "))
    add = no1 + no2
    print("Addition : ",add)

# addition()                               # calling the function     
# addition()        


for i in range(5):
    addition()

