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

# Another way
length = int(input("Enter the number of keys : "))
dict1 = {}
for i in range (length):
    key =  int(input("Enter the key : "))
    value = input("Enter the value : ")
    dict1[key] = value
print(dict1)

key1 = int(input("Enter a key to search : "))
for i in dict1:
    if key1 != key:
        break
else:
    print(key1,"is present in dict1 as a key")
