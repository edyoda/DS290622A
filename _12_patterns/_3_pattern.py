# 1 0 0 0
# 0 1 0 0
# 0 0 1 0
# 0 0 0 1

row = int(input("Enter number of rows: "))
col = int(input("Enter number of columns: "))
for i in range(row):
    for j in range(col):
        if i == j:
            print(1, end = " ")
        else:
            print(0, end = " ")
    print()
