str1 = input("Enter a string: ")
length = len(str1)

even_count = 0
odd_count = 0

for i in range(length):
    if i%2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Even character: ", even_count)
print("Odd character", odd_count)


