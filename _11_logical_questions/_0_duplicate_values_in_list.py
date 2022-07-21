# size=int(input("Enter the number of elements: "))
# lst1=[]
# for i in range(size):
#     num=int(input("Enter the element: "))
#     if num in lst1:
#         while num in lst1:
#             (print("The element is already present in the list"))
#             num=int(input("Enter the element: "))
#             continue
#     lst1.append(num)
# print(lst1)

size=int(input("Enter size"))
i=0
lst=[]
while i<size:
    value=int(input("Enter element"))
    if value in lst:
        print("Value exists in list, Please add another value")
    else:
        lst.append(value)
        i=i+1
print(*lst)
