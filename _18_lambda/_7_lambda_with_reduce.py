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


sum = lambda x,y : x+y
data = reduce(sum,lst)
print(data)



