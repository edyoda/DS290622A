# Dict comprehension - it is used to create new dict from another type of data

# str1 = "Python"
# dict_comp = {i.upper():i.lower() for i in str1}
# print(dict_comp)

# keys = [1,2,3,4,5]
# values = [10,20,30,40,50]
# dict1 = {k:v for k,v in zip(keys,values)}
# print(dict1)

# lst1=[1,2,3,4,5]
# lst2=[10,20,30,40,50]
# dict1={lst1[i]:lst2[i] for i in range(len(lst1)) }
# print(dict1)


# lst=[4,6,7,9,5]
# dict1={i:[n*i for n in range(1,11)] for i in lst}
# print(dict1)

lst1 = [1,2,3,4,5]
lst2 = [4,3,2,6,7]
data = [i for i in lst1 for j in lst2 if i == j]
print(data)

