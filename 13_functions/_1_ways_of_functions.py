# a function without a return type and without any arguments/parameter
def addition():                          # defining the function
    no1 = int(input("Enter number1 : "))
    no2 = int(input("Enter number2 : "))
    add = no1 + no2
    print("Addition : ",add)

# addition()

# function without a returntype but with arguments
# def subtraction(no1,no2):
#     sub = no1 - no2
#     print("Subtraction : ",sub)
    
# subtraction(4,3)

def multiplication():
    no1 = int(input("Enter number1 : "))
    no2 = int(input("Enter number2 : "))
    multi = no1 * no2
    return multi
    
# data = multiplication()
# print(data)

def division(no1,no2):
    div = no1//no2
    return div

no1 = int(input("Enter no1 : "))
no2 = int(input("Enter no2 : "))
result = division(no1,no2)
print(result)

length = len("Bharati")




