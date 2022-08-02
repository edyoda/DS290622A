lst = [3,6,1,1,3,5,7,98,54,67,63]

# lst1 = []
# def square(lst):
#     for i in lst:
#         lst1.append(i**2)
#     return lst1

# data = square(lst)
# print(data)

def square(lst):
    return lst**2

data = list(map(square,lst))
print(data)
