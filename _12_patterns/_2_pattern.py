# row_size = int(input("Enter the number of rows :"))
# temp1 = 1
# temp2 = 0
# for i in range(1,row_size+1):
#     for j in range(1,row_size+1):
#         if j %2 ==0:
#             print(temp2, end = "")
#         else:
#             print(temp1, end ="")
#     print()


for row in range(4):
    for col in range(4):
        if col == 1 or col == 3:
            print(0, end = " ")
        else:
            print(1,end = " ")
    print()


1 0 0 0
0 1 0 0
0 0 1 0
0 0 0 1
