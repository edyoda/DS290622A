# types of argument

# 1. required/positional argument
# 2. default argument
# 3. keyword argument
# 4. variable-length argument
#   4.1. Arbitrary positional argument
#   4.2. Arbitrary keyword argument





# required argument
# def add(no1,no2):
#     return no1 + no2

# add(4,5)




# default argument
# def add(no1=3,no2=9,no3=90):
#     result = no1 + no2
#     return result

# ans = add(6)
# print("Answer : ",ans)



# # keyword argument
# def add(no1,no2=0,no3=7):
#     print(no1)
#     print(no2)

# add(no3=7,no1=8)



# variable-length argument

# arbitary positional argument
# args
# tuple

# def users(*names):
#     print(type(names))
#     print(names[8][4])
#     for i in names:
#         print(i)

# users(1,2,3,4,5,"Bharati",True,6.7,[4,3,2,4,45,6657])


# Arbitrary Keyword Argument
# kwargs - kw - keywords
# dict

def users(**kwargs):
    print(type(kwargs))
    print(kwargs)

    for k,v in kwargs.items():
        print(k,"------>",v)

users(one="Bharati",two="Deen",three="Ram")