# str1 = input("Enter a string: ").lower()
# str2 = input("Enter a string: ").lower()

# list1 = str1.split()
# list2 = str2.split()

# for i in list2:
#     if i not in list1:
#         print(i, end = " ")

# for i in list1:
#     if i not in list2:
#         print(i, end = " ")


str=input("enter string")
str1=input("enter string")
count={}
for word in str.split():
    count[word]=count.get(word,0)+1
for word in str1.split():
    count[word]=count.get(word,0)+1
for word in count:
    if count[word]>=1:
        print(word)

