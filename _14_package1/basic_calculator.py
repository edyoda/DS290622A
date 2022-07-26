def add():
    print("******Add*****")
    no1 = int(input("Enter no1 : "))
    no2 = int(input("Enter no2 : "))
    addition = no1 + no2
    return addition

def sub():
    print("*******Sub*******")
    no1 = int(input("Enter no1 : "))
    no2 = int(input("Enter no2 : "))
    subtraction = no1 - no2
    return subtraction

print(__name__)

if __name__ == "__main__":
    sub()