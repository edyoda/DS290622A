# statement = input("Enter string: ")
# statement = statement.split()
# for i in statement:
#     if len(i) >= 7:
#         print(i)


str1 = input("Enter a string: ").lower()
lst = str1.split()

for i in lst:
    counter = 0
    for char in i:
        counter += 1
        if counter > 7:
            print(i)
            break
    
# 4456
# four thousand four hundred fifty six

