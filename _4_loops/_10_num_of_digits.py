num = int(input("Enter a value : "))
counter = 0
# 123 = 3 756

# mod = num % 10  # 3
# num = num // 10 # 12
# counter += 1    # 1

# mod = num % 10  # 2
# num = num // 10 # 1
# counter += 1    # 2

# mod = num % 10  # 1
# num = num // 10 # 0
# counter += 1    # 3

while num != 0:
    mod = num % 10  # 3
    num = num // 10 # 12
    counter += 1    # 1

print("Length : ",counter)

# 456 = 654