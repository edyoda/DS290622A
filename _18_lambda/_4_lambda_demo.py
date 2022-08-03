# Lambda Function
# it is an anonymous function
# it is a function without a name
# it can have any number of arguments but can have only one expression (condition)
# it helps us to create one liner function

# Function
# we have to define the name of the function
# return statement is required
# cannot be passed as a parameter
# complex

# Lambda
# no function name is required
# no return statement is required
# can be define as parameter
# simple
# one liner

def fun(a,b):
    return a+b

add = fun(4,5)
print("Result : ",add)

# syntax : lambda <argument,argument> : <expression>

data = lambda a,b : a + b
result = data(4,5)
print("Result : ",result)

