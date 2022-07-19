# lst1 = [4,6,10,8,12]
# lst2 = [6,7,9,11,10]


# for i in lst1:
#     if i not in lst2:
#         print(i)
# print()
# for j in lst2:
#     if j not in lst1:
#         print(j)

# lst1=[2,3,4,5]
# lst2=[4,5,6,7]
# for i in lst1:
#     if i in lst2:
#         lst2.remove(i)
   
# print(lst2)

data=int(input("Enter a number of elements in list1: "))
lst1=[]
for i in range(data):
 value=int(input("Enter an element: "))
 lst1.append(value)
data=int(input("Enter a number of elements in list2: "))
lst2=[]
for i in range(data):
 value=int(input("Enter an element: "))
 lst2.append(value)
new_lst=lst1+lst2
result=[]
for i in new_lst:
    if i not in result:
        result.append(i)
print(result)
