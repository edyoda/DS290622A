file = open("demo.txt")
file.close() #! Close the file

is_close = file.closed
print("Closed : ",is_close)

file_name = file.name
print("File name : ",file_name)

mode = file.mode
print("Mode : ",mode)