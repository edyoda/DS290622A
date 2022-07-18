data=int(input("Enter the size of the list"))
lst=[]
for i in range(data):
 value=int(input("Enter an element: "))
 lst.append(value)

largest_number = lst[0]
for num in lst:
    if num > largest_number:
        largest_number = num
    
print("The largest number in the list is:",largest_number)
