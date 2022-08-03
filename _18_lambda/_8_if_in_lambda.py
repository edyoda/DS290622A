# str1 = "Bharati"

# res = lambda data : True if data.startswith('b') else False
# print(res(str1))

# lst = [5,6,2,5,7,9,4,2]
# oddEven = lambda lst : "Even" if lst%2 == 0 else "Odd"
# data = list(map(oddEven,lst))
# print(data)



lst = [12,15,17,30,33,25]
divisible = lambda num : num if num%3 == 0 and num%5 == 0 else None
data = list(filter(divisible,lst))
print(data)


lst=[3,15,30,4]
oper=lambda num:num%3==0 and num%5==0
data=list(filter(oper,lst))
print(data)


lst = ["apple","mango","banana"]
rev=list(map(lambda str1: str1[::-1],lst))
print(rev)
