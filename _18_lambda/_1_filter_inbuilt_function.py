lst = [6,7,43,5,7,78,3,5,6,7]

# def even(lst):
#     lst1 = []
#     for i in lst:
#         if i%2==0:
#             lst1.append(i)
#     return lst1

# even_nos = even(lst)
# print(even_nos)

def even(lst):
    return lst%2==0

data = list(filter(even,lst))
print(data)

# for i in data:
#     print(i)

