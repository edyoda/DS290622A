try:
    str1 = None
    print(len(str1))
    print(10/0)
except ZeroDivisionError as ex:
    print("We got zero division error!")
except ValueError as ex:
    print("We got value error!")
except Exception as ex:
    print("We got exception")


