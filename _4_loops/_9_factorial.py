# 5! = 5*4*3*2*1

# num = int(input("Enter a number : "))

# fact = 1
# if num == 0:
#     fact = 1
# else:
#     for i in range(1,num+1):
#         fact *= i #24*5 = 120

# print(fact)


number = int(input("Enter the number: ")) #5
og = number
for i in range(1,number):
    number = number * i #30*4 = 120
print(number)

