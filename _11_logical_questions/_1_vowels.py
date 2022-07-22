str1 = input("Enter a string: ")

vowels = ['a','e','i','o','u']

for i in str1.lower():
    if i in vowels:
        print(i)

