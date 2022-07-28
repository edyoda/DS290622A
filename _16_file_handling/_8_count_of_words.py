# file_name = input("Enter file name: ")
# num_words = 0
# with open(file_name, 'r') as f:
#     for line in f:
#         words = line.split()
#         num_words += len(words)
# print("Number of words:")
# print(num_words)



# file = open(input("Enter a file name: "))

# count  = 0
# dict1 = {}
# for line in file:
#     line1 = line.replace(","," ")
#     line1 = line1.rstrip().split()
#     for word in line1:
#         count += 1
#         dict1[word] = dict1.get(word,0) + 1
# file.close()

# for k,v in dict1.items():
#     print(f"{k} is printed {v} times")

# print("Total no. of words in file: ", count)




file_location = input("Enter file location : ")
data = input("Enter your data : ")
with open(file_location) as file:
    res = len(data.split() or data.split(","))

print ("The number of words in data are : ", res)





string=input("Enter file name")
file=open(string,"r")
data=file.read()
lst=[]
for i in data.split():
    lst.extend(i.split(","))
print(len(lst))
file.close()

