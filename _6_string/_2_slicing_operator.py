# slicing operator 
# syntax : [start_range:end_range:step]
# it is used to get the substring from string

str1 = "Python is a programming language"

# substring = str1[2:6]
# print(substring)

# substring = str1[:4]
# print(substring)

# substring = str1[2:]
# print(substring)

# substring = str1[:]
# print(substring)

# substring = str1[-1:]
# print(substring)

# substring = str1[1:6:2]
# print(substring)

# substring = str1[::-1]
# print(substring)

# for i in str1:
#     print(i)

# str1 = str("Dharani")
# counter = 0
# for word in str1:
#     counter = counter+1
# print("Length of a string :",counter)

size = int(input("Enter the size : "))

lst = []
for i in range(size):
    value = int(input("Enter the element : "))
    lst.append(value)

print(lst)
