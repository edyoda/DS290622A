# for i in range(1,7):
#     for j in range(i,6):
#         print(" ", end = "")
#     for j in range(i): 
#         print(" *", end = "")
#     print()
    
# for i in range(5,10):
#     for j in range(4,i):
#         print(" ", end = "")
#     for j in range(i,10):
#         print(" *", end = "")
#     print()

for i in range(1,5):
    for j in range(5, 0, -1):
        if j > i:
            print(" ", end=' ')
        else:
            print(" *", end=' ')
    print()
for i in range(3, 0, -1):
    for j in range(1,5):
        if j > i:
            print(" ", end=' ')
        else:
            print("* ", end=' ')
    print()
