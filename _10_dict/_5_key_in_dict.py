length = int(input("Enter a number: "))

dict1 = {}
for i in range(length):
    key = int(input("enter a key: "))
    value = input("enter a value: ")
    dict1[key] = value

key_1 = int(input("Enter the key you want: "))

if key_1 in dict1:
    print("The key is present in dictionary")
    
print(dict1.get(key_1,"The key is not present in dictionary"))
