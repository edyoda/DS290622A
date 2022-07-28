f = open("demo1.txt")
lst = []
count = 0
for line in f:
    lst.append(line)
    count += 1 

print(lst)
print(count)


