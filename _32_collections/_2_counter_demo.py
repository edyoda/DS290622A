# Counter

# it's a child class of dict class
# it will consider elements as key
# and count of elements as value

# ["a","a","a","c","b","b"]

# a : 3
# c : 1
# b : 2

from collections import Counter

lst = ["a","a","a","c","b","b"]

counter_obj = Counter(lst)
print(counter_obj)

counter_obj1 = Counter(a=4,b=9,c=10)
print(counter_obj1)

counter_obj1 = Counter({'a': 3, 'b': 2, 'c': 1})
print(counter_obj1)

