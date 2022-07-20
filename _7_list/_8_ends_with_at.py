# length = int(input("Enter a number: "))

# lst = []
# for i in range(length):
#     num = input("Enter an element: ")
#     lst.append(num)
# print("Words ending with 'at': ")
# for word in lst:
#     if word.endswith("at"):
#         print(word)

# size=int(input("Enter size:"))
# lis=[]
# for i in range(size):
#     value=input("Enter String:")
#     lis.append(value)
# at_list=[]
# for i in lis:
#     if i[-2:].lower() == "at":
#         at_list.append(i)
# print(*at_list)


size = int(input("Enter the size : "))
lst = []
for i in range(1,size+1):
    string_input = input("Enter the String : ")
    lst.append(string_input)

end = ["at","AT","aT","At"]
for unit in lst:
    if unit[-2:] in end:
        print(unit)

