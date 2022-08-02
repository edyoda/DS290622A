from functools import reduce

lst = [6,73,2,4,6,7,8,9,5]

# def sum_list(lst):
#     sum_off = 0
#     for i in lst:
#         sum_off += i
#     return sum_off

# data = sum_list(lst)
# print(data)

# def sum(lst,lst1):
#     return lst+lst1

# data = reduce(sum,lst)
# print(data)


lst = ["Dog","Cat","Lion","Cheetah","Donkey","Monkey"]

# def startd(m):
#     return m[0].upper()=="D"
# data=list(filter(startd,lst))
# print(data)

import re
def identify(lst):
    res = re.findall("^D|d",lst)
    return res
data = list(filter(identify,lst))
print(data)

lst = ["dog", "cat", "Donkey", "cheetah"]
def func1(str1):
    return str1.lower().startswith("d")

result = list(filter(func1,lst))
print(result)



