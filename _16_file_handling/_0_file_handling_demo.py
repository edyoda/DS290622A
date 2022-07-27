# File Handling
# - it is used to store data permanently in the file.

# Type of files
# 1. Text File
# 2. Binary File (image,audio,video)

# Modes for text files 
# r -> read mode , bydefault mode, used to the read the data from file
# w -> write mode , it creates the file, if file doesn't exist , it also allows you to write the data in file. If file already exist then it will replace it.
# a -> append mode , it creates the file, if it doesn't exist and also allows to write the data in it.
# r+ -> read/write mode , it allows to read and write the data in file
# w+ -> write/read mode , it creates the file, it replaces the file if it already exist and it allows both to read and write the data in file 
# a+ -> append/read mode

# Modes for binary files
# rb
# wb
# ab
# rb+
# wb+
# ab+

# write mode 
# open(filename,mode)
# file = open("demo.txt","w")
# # file.write("Hello Student!!!")
# # file.write("Good Evening All!!!")
# file.write("Ok Bye! Good Night!")


# # read mode
# file = open("demo.txt","r")
# data = file.read()
# print(data)


# # append mode
# file = open("demo1.txt","a")
# # file.write("Heyy")
# file.write("Students!")



# w+ mode
file = open("demo2.txt","w+")
# file.write("Python")
file.write("Programming")
file.seek(0,0)
data = file.read()
print(data)



# # r+ mode
# file = open("demo2.txt","r+")
# file.write("Java")
# data = file.read()
# print(data)



# # +a mode
# file = open("demo3.txt","a+")
# # file.write("Hey")
# file.write("Ram")
# data = file.read()
# print(data)
