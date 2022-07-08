# Type Casting - where you can convert one datatype into another datatype
# int()
# float()
# str()
# bool()
# complex()
# list()
# set()
# tuple()
# dict()

# num = 100

# print("int into int : ",int(num),"------->", type(int(num)))
# print("int into float : ",float(num),"------>", type(float(num)))
# print("int into str : ",str(num),"------>", type(str(num)))
# print("int into bool : ",bool(num),"------>", type(bool(num)))
# print("int into complex : ",complex(num),"------>", type(complex(num)))


# num = 100.8

# print("float into int : ",int(num),"------->", type(int(num)))
# print("float into float : ",float(num),"------>", type(float(num)))
# print("float into str : ",str(num),"------>", type(str(num)))
# print("float into bool : ",bool(num),"------>", type(bool(num)))
# print("float into complex : ",complex(num),"------>", type(complex(num)))

# name = "Edyoda"
# # name = "101"

# # print("str into int : ",int(name),"------->", type(int(name))) # we cannot convert string into int if it containes alphabet but if it only contains digit then we can convert it into int
# # print("str into float : ",float(name),"------>", type(float(name))) # we cannot convert string into int if it containes alphabet but if it only contains digit then we can convert it into int
# print("str into str : ",str(name),"------>", type(str(name)))
# print("str into bool : ",bool(name),"------>", type(bool(name)))
# print("str into complex : ",complex(name),"------>", type(complex(name))) # we cannot convert string into int if it containes alphabet but if it only contains digit then we can convert it into int


# human = False # True = 1  and False = 0

# print("bool into int : ",int(human),"------->", type(int(human)))
# print("bool into float : ",float(human),"------>", type(float(human)))
# print("bool into str : ",str(human),"------>", type(str(human)))
# print("bool into bool : ",bool(human),"------>", type(bool(human)))
# print("bool into complex : ",complex(human),"------>", type(complex(human)))

# com = 10+9j

# # print("complex into int : ",int(com),"------->", type(int(com)))
# # print("complex into float : ",float(com),"------>", type(float(com)))
# print("complex into str : ",str(com),"------>", type(str(com)))
# print("complex into bool : ",bool(com),"------>", type(bool(com)))
# print("complex into complex : ",complex(com),"------>", type(complex(com)))


lst = [10,2,6,3,1,5,6,7,8,8,6]
print(lst)

unique = set(lst)
print(unique,"----->",type(unique))

lst1 = list(unique)
print(lst1,"----->",type(lst1))

unmodifiable = tuple(lst1)
print(unmodifiable,"----->",type(unmodifiable))

