import memory_profiler as memory

def fun(n):
    lst = []
    for i in range(n):
        lst.append(i)
    return lst

print("Before calling function memory is : ",memory.memory_usage())
fun(100000000)
print("After calling function memory is : ",memory.memory_usage())

def gen(n):
    for i in range(n):
        yield i

print("Before calling function memory is : ",memory.memory_usage())
gen(100000000)
print("After calling function memory is : ",memory.memory_usage())