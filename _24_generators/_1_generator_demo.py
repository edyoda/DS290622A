# Generators

# generators are function
# it is memory efficient
# do not allocate memory to all the objects at the same time
# it yields the data and returns the elements of data when it is demanded

def fun(n):
    yield n*2

result = fun(10)
print(next(result))

gen = (2*i for i in range(1,11)) # 2,4,6,8,10,12,14,16,18,20
print(next(gen))
print(next(gen))
