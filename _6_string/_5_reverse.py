user_input = input("Enter a string: ")
str_len = len(user_input)
reversed = ""
for i in range(str_len):
    reversed += user_input[i]
print("Input :",user_input)
print("Output :",reversed)

my_str=input("enter string")
str=""
for i in my_str:
    str+=i
print(str) 

word = int(input("Enter a word : "))
for i in range(len(word)-1,-1,-1):
    print(word[i],end="")


