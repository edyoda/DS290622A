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

# a11 a12 a13 a14
# a21 a22 a23 a24 
# a31 a32 a33 a34 
# a41 a42 a43 a44

A B C D
A B C D
A B C D 
A B C D 
