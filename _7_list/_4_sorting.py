list_length = int(input("Enter a number: "))

lst = []
for i in range(list_length):
    num = int(input("Enter a number: "))
    lst.append(num)

length = len(lst)
for i in range(length): 
    for j in range(i+1,length):
        if lst[i] >= lst[j]:
            lst[i],lst[j] = lst[j],lst[i] 

print(lst)
print(lst[0])
print(lst[-1])

