# context manager

# it automatically closes the file
with open("demo1.txt","w") as file: #file = open("demo1.txt")
    file.write("Hello")
    file.close()

# file = open("demo2.txt")
# print(file.closed)