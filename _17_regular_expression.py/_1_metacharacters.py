# Metacharacter

import re

# data = "Hello"
# res = re.findall("[a-z]",data) # it will check if string contains small characters
# print(res)

# data = "Hello"
# res = re.findall("[A-Z]",data) # it will check if string contains capital characters
# print(res)

# data = "Hello"
# res = re.findall("[A-z]",data) # it will check if string contains both small/captial characters
# print(res)

# data = "Hello123"
# res = re.findall("[a-zA-Z]",data) # it will check if string contains small/capital characters
# print(res)

# data = "Hello"
# res = re.findall("[a-e]",data) # # it will check if string contains characters from 'a'-'e'
# print(res)

# data = "Hello"
# res = re.findall("[A-E]",data) # it will check if string contains characters from "A" - "E"
# print(res)

# data = "Hello123"
# res = re.findall("\d",data) # it will check if string contains digits
# print(res)

# data = "Hello Pranav!"
# res = re.findall("H...o",data) # search for the string which starts with 'h' and ends with 'o' and can have any 3 characters in between them
# print(res)

# data = "Hello Pranav!"
# res = re.findall("^H",data) # checks if the string starts with 'H'
# print(res)

# data = "Hello Pranav!"
# res = re.findall("Pranav!$",data) # checks if the string ends with 'Pranav!'
# print(res)

# data = "Heo Pranav!"
# res = re.findall("He.*o",data) # checks if the string starts with 'He' and ends with 'o' and in between it can have 0 or more characters
# print(res)

# data = "Hello Pranav!"
# res = re.findall("He.+o",data) # checks if the string starts with 'He' and ends with 'o' and in between it can have 1 or more characters
# print(res)

# data = "Heo Pranav!"
# res = re.findall("He.?o",data) # checks if the string starts with 'He' and ends with 'o' and in between it can have 0 or 1 character
# print(res)

# data = "Hello Pranav!"
# res = re.findall("He.{2}o",data) # checks if the string starts with 'He' and ends with 'o' and in between it can have 2 characters
# print(res)

# data = "Python is a programming language!" # checks if string contains "is"
# res = re.findall("is",data)
# print(res)

# data = "Python is a programming language!" # checks if string contains "is","language","python"
# res = re.findall("is|language|python",data)
# print(res)

# data = "responsibility"
# res =  re.findall("re.*i",data)
# print(res)