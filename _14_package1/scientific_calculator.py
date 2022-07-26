# from <file_name> import <function,class,variable>
# from basic_calculator import add
# from basic_calculator import *
# import basic_calculator
import basic_calculator as basic

def multi():
    print("******Multi*****")
    no1 = int(input("Enter no1 : "))
    no2 = int(input("Enter no2 : "))
    multiplication = no1 * no2
    return multiplication


if __name__ == "__main__":
    result = basic.add()
    print(result)

    result = multi()
    print(result)
