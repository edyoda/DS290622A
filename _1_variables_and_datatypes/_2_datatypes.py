"""
Datatypes
1. int    - whole number
2. float  - decimal values
3. str    - word,character,para,single statement
4. bool   - True,False
5. complex - real + imaginary value
6. list    
7. tuple
8. set
9. dict
10. NoneType
"""

# # int
# not iterable
# num = -20
# print(type(num))

# # float
# not iterable
# price = 67.50
# print(type(price))

# str
# iterable
# name = "Bharati"
# print(type(name))

# bool
# not iterable
# human = True
# print(type(human))

# complex
# not iterable
# comp = 7+9j
# print(type(comp))

# list
# []
# it can store heterogenous data
# duplicates are allowed
# indexed based
# it is modifiable
# it is ordered
# iterable
# lst = [5,6,3,5,7,2,1,"Bharati","A",8.9,True,5]
# print(lst)
# print(type(lst))
# print(lst[7])
# lst[7] = "Kavirajan"
# print(lst[7])


# tuple
# ()
# duplicates are allowed
# indexed based
# not modifiable
# it can store heterogenous data
# it is ordered
# iterable
# tup = (4,5,3,5,6,"Edyoda")
# print(tup)
# print(type(tup))
# print(tup[5])
# tup[5] = "Coder" # cannot modify tuple

# set
# {}
# it is unordered instead it displays it in sequential manner
# it doesnot duplicate values
# it is non-indexed based
# it stores heterogenous data
# iterable
# set_demo = {4,5,6,3,7,1,2,4,5,"Bharati"}
# print(set_demo)
# print(type(set_demo))


# dict 
# {key:value} ---> item
# key should always be unique
# values can be duplicate
# non-indexed based
# it is modifiable
# iterable
dict_demo = {"one":"Bharati","two":"Mohit","three":"Deepak","four":"Bharati"} 
print(dict_demo)
print(type(dict_demo))
print(dict_demo["one"])
dict_demo["one"] = "Rohan"
print(dict_demo["one"])


# NoneType
# not iterable
# language = None
# print(language)
# print(type(language))



