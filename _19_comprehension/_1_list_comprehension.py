# List Comprehension -it is use for creating new list from another list

# for i in lst:
#     if conditon:
#         expression

# syntax : 
# [expression for i in lst if condition]



# nums = [1,2,4,5,6,7]

# lst = []
# for i in nums:
#     lst.append(i)

# print(lst)

# data = [i for i in nums]
# print(data)



nums = [10,49,8,90,43,89,100,24]

# even = []
# for i in nums:
#     if i%2==0:
#         even.append(i)

# print(even)

# data = [i for i in nums if i%2==0]
# print(data)

# str1 = Python
# ['P','y','t','h','o','n']


# str1=input("Enter string :")
# result=([i for i in str1])
# print(result)

# lst = ["apple","mango","aeroplane","ac","laptop","diary","mobile"]
# data=[i for i in lst if i.lower().startswith("a") and len(i)>4]
# print(data)

lst = [10,4,56,34,5,6,67]
new_lst = [lst[i] for i in range(len(lst)) if i not in [0,2,4,6]]
print(new_lst)

lst1 = [10,15,20,25,30,35]
lst2 = [i for i in lst1[1::2]]
print(lst2)

nums=[5,6,2,5,75,93,42,2]
data=[nums[i] for i in range(len(nums)) if i%2!=0 ]
print(data)

