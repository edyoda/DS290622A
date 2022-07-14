for i in range(1,11):
    for j in range(1,11):
        mul = i * j
        if mul<10:
            print(mul, end = "   ")
        else:
            print(mul, end = "  ")
    print()
