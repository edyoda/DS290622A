set1 = {5,4,2,1,6,8}
set2 = {5,6,3,2,4,6,35,656,}

# set3 = set2.difference(set1) # set2-set1 , returns uncommon value from set2
# print(set3)

# set2.difference_update(set1) # set2 -set1 , same as above , no third variable required
# print(set2)

# set3 = set2.intersection(set1) # returns common values
# print(set3)

# set2.intersection_update(set1) # same as above, no third variable required
# print(set2)

# set3 = set1.union(set2) # combines both the set into one set
# print(set3)

# set3 = set1.issuperset(set2) # checks if all the elements of set2 is present in set1
# print(set3)

# set3 = set1.issubset(set2) # checks if all the element of set1 is present in set2
# print(set3)

# set_demo.add(3) #to add the element in set
# print("Set : ",set_demo)

# set_demo.remove(8) #removes the passed object
# print("Set : ",set_demo)

# set_demo.discard(8) #removes the object and also it doesnot raise any error when object is not present in set
# print("Set : ",set_demo)

# set_demo1 = set_demo.copy() # creates copy of set
# print(set_demo1)

# set_demo.clear() #removes all the elements
# print(set_demo)

for i in set1:
    print(i)