# types of variables
# 1. local variable
    # - are the variables which are define inside the function
    # - it's scope is within the function itself
    # - you cannot access it outside the function directly
    # - even parameters are local variable

# 2. global variable
    # - are the variables which are define outside the function
    # - it's scope is throughout the python file

from ctypes import addressof


# rno = 90                # global variable

# def info():
#     name = "Bharati"    # local variable
#     global address
#     address = "Mumbai"
#     print(f"Hi {rno}, {name}, {address}")
#     return name

# data = info()
# print(data)

# print("Rno : ",rno)
# print("Address : ",address)

def variables():
    global name
    name = "Edyoda"
    # name = "Coder"
    # print(name)

variables()
print(name)


