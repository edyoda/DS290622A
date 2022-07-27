file = open("demo.txt","w")
# data = file.read() # read the whole data
# print(data)

# data = file.read(5) # reads 5 characters
# print(data)

# data = file.readline() # only reads the first line
# print(data)

# data = file.readlines() # it returns list of lines
# print(data)

# for i in file:
#     print(i)

# file.write("Hello")

lst = ["Hello All","Good Night","Bye"]
file.writelines(lst)