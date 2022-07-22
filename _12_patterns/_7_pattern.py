num_rows = int(input('Enter the number of rows'))
for i in range (0,num_rows):  
    for j in range (num_rows,i,-1):  
        print("* ", end="")
    print()
