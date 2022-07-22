for i in range (65,69):
    # inner loop
    for j in range(65,69):
        print(chr(j),end=" ")
    print()



row=int(input("Enter the number of rows :"))
col=int(input("Enter the number of columns :"))
for i in range(row):
    k=65
    for j in range(col):
        print(chr(k),end=' ')
        k+=1
    print()
