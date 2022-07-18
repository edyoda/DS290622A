# string=input("Enter a string")
# lst=list(set(string))
# for i in lst:
#     if string.count(i)>1:
#         print(i,end=" ")

name = "dharani"
duplicates = []
for char in name:
        if name.count(char) > 1:
            if char not in duplicates:
                duplicates.append(char)
print(*duplicates)

# str1 = input("Enter a string: ")

# count = {}
# for i in str1:
#     if i not in count:
#         count[i] = 1
#     else:
#         count[i] = count[i] + 1

# for k,v in count.items():
#     if v > 1:
#         print(k)


# word=input("Enter a string :")
# lst=list(set(word))
# for i in lst:
#     count=0
#     for char in word:
#         if i==char:
#             count+=1
#             if count>1:
#                 print("",i,"is present",count,"times")
      


