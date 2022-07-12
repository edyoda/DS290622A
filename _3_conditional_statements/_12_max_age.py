from functools import total_ordering
from sys import set_coroutine_origin_tracking_depth


age1 = int(input("Enter age : "))
age2 = int(input("Enter age : "))
age3 = int(input("Enter age : "))

if age1>age2 and age1>age3:
    print("The oldest is ", age1)
elif age2>age1 and age2>age3:
    print("The oldest is ", age2)
elif age3>age1 and age3>age2:
    print("The oldest is ", age3)
else:
    print("All are of same age")


if age1<age2 and age1<age3:
    print('age1 is youngest')
elif age2<age1 and age2<age3:
    print('age2 is youngest')
elif age3<age1 and age3<age2:
     print('age3 is youngest')
else:
    print("All are of same age")



age1 = int(input("Enter age : "))
age2 = int(input("Enter age : "))
age3 = int(input("Enter age : "))

# if age1 == age2 and age2 == age3:
#     print("All are of same age")
# else:
#     lst = []
#     lst.append(age1)
#     lst.append(age2)
#     lst.append(age3)

#     minimum = min(lst)
#     maximum = max(lst)
#     print("Minimum age is ", minimum)
#     print("Maximum age is ", maximum)






