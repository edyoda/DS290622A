num = int(input("Enter the number of elements: "))
lst = []
for i in range(num):
    ele = int(input())
    lst.append(ele)

ele1 = int(input("Enter an element : "))
if ele1 in lst:
    print(ele1,"is there in", lst)
else:
    print(ele1,"is not there in", lst)
