# def fun(n):
#     sum = 0
#     for i in range(1,n+1):
#         sum += i
#     return sum

# print(fun(3))

def fun(n):
    if n == 0:
        return 0
    return n + fun(n-1)
    
print(fun(5))

# 5 + fun(4)
# 5 + 4 + fun(3)
# 5 + 4 + 3 + fun(2)
# 5 + 4 + 3 + 2 + fun(1)
# 5 + 4 + 3 + 2 + 1 + fun(0)

def factorial(num):

    if num == 0:
        return 1
    return num * factorial(num-1)

print(factorial(5))


def digital_root(n):
    lst = []
    while n != 0:
        mod = n%10
        lst.append(mod)
        n = n//10
    if sum(lst) < 10:
        return sum(lst)
    else:
        return(digital_root(sum(lst)))
    
print(digital_root(123))

def digital_root(n):
    n=str(n)
    sums=0
    for i in list(n):
        sums+=int(i)    
    if sums<10:
        return sums
    else:
        return digital_root(sums)
        
a=digital_root(493193)
print(a)

str1 = "It's raining outside"
# o/p = raining






