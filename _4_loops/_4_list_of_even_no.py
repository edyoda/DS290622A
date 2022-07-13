start_range = int(input("Enter the start range : "))
end_range = int(input("Enter the end range"))

for i in range(start_range,end_range+1):
    if i % 2 == 0:
        print(i)