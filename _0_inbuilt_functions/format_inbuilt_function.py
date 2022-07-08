greetings = "Good Evening"
name = "Rohan"
age = 20
# Good Evening Rohan! Your age is 20

print(greetings,name,"! Your age is",age)

print(f"{greetings} {name} ! Your age is {age}")

# Default Formatting
print("{} {} ! Your age is {}".format(greetings,name,age))

# Keyword Formatting
print("{a} {b} ! Your age is {c}".format(c = age,a = greetings,b = name))

# Positional Formatting
print("{1} {2} ! Your age is {0}".format(age,greetings,name))

# String Alignment
print("|{:<20}|{:^50}|{:>10}|".format("Left","Center","Right"))


