from re import U


str1 = "python is a programming language"
print("Orginal String : ",str1)

# captial = str1.capitalize()    # ---> used to convert initial letter into capital
# print("Capitalize : ",captial)

# ends_with = str1.endswith("programming language")# ---> use to check if the string ends with string provided as parameter
# print("Ends with : ",ends_with)

# starts_with = str1.startswith("Python") # ---> use to check if the string starts with string provided as parameter 
# print("Starts with : ",starts_with)

# index_demo = str1.index('i') # ---> will return the index of value passed as parameter
# print("Index : ",index_demo)
 
# length = len(str1) # ---> used to find the count of characters in string, it starts from 1
# print("Length : ",length)

# strip_demo = str1.strip() # ---> used to remove starting and ending spaces 
# print("Strip : ",strip_demo)

# lstrip_demo = str1.lstrip() # ---> used to remove left end spaces
# print("lstrip : ",lstrip_demo)

# rstrip_demo = str1.rstrip() # ---> used to remove right end spaces
# print("rstrip : ",rstrip_demo)

# title_demo = str1.title() # ---> it will convert the initial of every word into capital letter
# print("Title : ",title_demo)

# is_title_demo = str1.istitle() # ---> it will check if string is following title pattern or not
# print("Is title : ",is_title_demo)

# lst = ["Python","Java","Cpp"] # ---> to concat multiple strings together
# join_demo = "$".join(lst)
# print("Join : ",join_demo)

# replace_demo = str1.replace("python","java") # ---> to replace the string
# print("Replace : ",replace_demo)

# replace_demo = str1.replace("o","e") # ---> to replace the string
# print("Replace : ",replace_demo)

# split_demo = str1.split(" ") # ---> to split the string on the bases of provided parameter
# print("Split : ",split_demo)

# for i in split_demo:
#     print(i)

# swap_demo = str1.swapcase() # ---> swaps the case of the string
# print("Swap : ",swap_demo)

# is_digit_demo = str1.isdigit() # ---> checks if every character of string is digit 
# print("is digit : ",is_digit_demo)

# is_alpha_demo = str1.isalpha() # ---> checks if every character is a letter
# print("is alpha : ",is_alpha_demo)

# is_alpha_num_demo = str1.isalnum() # ---> check if it atleast as one character, it can be anything alpha,numeric or alpha-numeric
# print("Is alphanum : ",is_alpha_num_demo)

# count_demo = str1.count("o") # ---> returns the count of the string provided as argument
# print("Count : ",count_demo)

# contains_demo = str1.__contains__("the") # ---> checks if the argument is present in the string
# print("Contains : ",contains_demo)

# upper_demo = str1.upper() # ---> converts the string into capital letters
# print("Upper : ",upper_demo)

# lower_demo = str1.lower() # ---> converts string into lower letters
# print("Lower : ",lower_demo)

# is_lower_demo = str1.islower() # ---> checks if the string is in lower letter
# print("Is lower : ",is_lower_demo)

# is_upper_demo = str1.isupper() # ---> checks if the string is in upper letters
# print("Is upper : ",is_upper_demo)

# enumerate_demo = enumerate(str1) # ---> it returns the tuple of key and value
# print("Enumerate : ",list(enumerate_demo))
 
# ord_demo = ord("A") # ---> it returns the ascii code of the character passed as parameter
# print("Ord : ",ord_demo)

find_demo = str1.find("o",7,15)
print("Find : ",find_demo)

# find_demo = str1.index("Bharati")
# print("Find : ",find_demo)