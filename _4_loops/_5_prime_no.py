# num = int(input("Enter the number: "))
# prime = True

# for i in range(2, num): #5
#     if(num%i == 0):
#         prime = False
#         break
# if prime:
#     print("This number is Prime")
# else:
#     print("This number is not Prime")

num=int(input("enter a number :"))
for i in range(2,int( num /2)+1):
    if (num % i)==0:
        print("it is not a prime no")
        break
else:
    print("it is a prime")

