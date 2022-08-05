# Set Comprehension - it is used to create new set from another set,list,tuple

nums = [1,2,3,4,5,6,7,8,9,10,2,4,10]
even = {i for i in nums if i%2==0}
print(even)