import re

# data = "Python is high level programming language"
# res = re.findall("\APython",data) # it checks if string starts with "Python"
# print(res)

# txt = "The rain in Spain"
# #Check if "rai" is present at the beginning of a WORD:
# x = re.findall(r"\brai", txt)
# print(x)

# txt = "The rain in Spain"
# #Check if "ain" is present at the end of a WORD:
# x = re.findall(r"\Bain", txt)
# print(x)

# txt = "The rain in Spain123"
# #Check if digits are present in the data
# x = re.findall(r"\d", txt)
# print(x)

# txt = "The rain in Spain123"
# #Check if non-digits are present in the data
# x = re.findall(r"\D", txt)
# print(x)

# txt = "The rain in Spain123"
# #Check if spaces are present in the data
# x = re.findall(r"\s", txt)
# print(x)

# txt = "The rain in Spain123"
# #Check if non-space are present in the data
# x = re.findall(r"\S", txt)
# print(x)

# txt = "The rain in Spain123_@@@@@"
# #Check if A-z,0-9,_ are present in the data
# x = re.findall(r"\w", txt)
# print(x)

# txt = "The rain in Spain123 @@@%$&%*^"
# #Check if A-z,0-9,_ are not present in the data
# x = re.findall(r"\W", txt)
# print(x)

txt = "The rain in Spain"
#Check if data ends with "Spain"
x = re.findall(r"Spain\Z", txt)
print(x)

