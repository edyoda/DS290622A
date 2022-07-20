length = int(input("Enter a size: "))

dict1 = {}
for i in range(length):
    key = int(input("enter a key: "))
    value = input("enter a value: ")
    dict1[key] = value
    
print(dict1)
