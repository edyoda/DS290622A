# # row = int(input("Enter number of rows: "))
# for i in range(4): #i = 1
#     for j in range(i,4): #j = 1
#         print(" ", end = " ")
#     for k in range(i):  #k=1
#         print("*", end = " ")
#     print()


for i in range(1,5):
    for j in range(5, 0, -1):
        if j > i:
            print(" ", end=' ')
        else:
            print("*", end=' ')
    print("")





