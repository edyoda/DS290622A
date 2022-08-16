str1 = None
try:
    print(len(str1))
except Exception as ex:
    print(ex)
    str1 = input("Enter string : ")
    print(len(str1))

print("End!")

