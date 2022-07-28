# seek() ---> it allows you to the change the position of the cursor
# seek(offset,from_what)
# offset - no. of position to move forward
# from_what - point of reference

# from_what accepts only 3 parameters
# 0 - beginning of the file
# 1 - current position of the file
# 2 - end of the file

# from_what default value is 0
# therefore, the reference point cannot be set to the current position or end position,
# in the text mode, except when the offset is 0

file = open("demo.txt","w")
cur_pos = file.tell()
print("Current Position before : ",cur_pos)
file.seek(4,0)
cur_pos = file.tell()
print("Current Position after : ",cur_pos)

