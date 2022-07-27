# tell() ---> it tells you the current position of cursor in the file

# file = open("test.txt","w")
# cur_pos = file.tell()
# print("Current Position Before Writing : ",cur_pos)
# file.write("Python")
# cur_pos = file.tell()
# print("Current Position After Writing : ",cur_pos)



# file = open("test.txt","r")
# cur_pos = file.tell()
# print("Current Position Before Reading : ",cur_pos)
# data = file.read()
# cur_pos = file.tell()
# print("Current Position After Reading : ",cur_pos)



# file = open("test.txt","a")
# cur_pos = file.tell()
# print("Current Position Before Reading : ",cur_pos)
# file.write("Hello")
# cur_pos = file.tell()
# print("Current Position After Reading : ",cur_pos)
# file.write("Ram")
# cur_pos = file.tell()
# print("Current Position After Reading : ",cur_pos)



file = open("test.txt","r+")
cur_pos = file.tell()
print("Current Position Before Reading : ",cur_pos)
data = file.read()
cur_pos = file.tell()
print("Current Position After Reading : ",cur_pos)
