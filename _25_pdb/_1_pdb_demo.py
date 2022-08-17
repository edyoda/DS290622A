import pdb

def addition(no1,no2):
    add = no1 + no2 
    return add

pdb.set_trace()
if __name__ == "__main__":
    no1 = int(input("Enter a no1 : "))
    no2 = input("Enter a no2 : ")
    res = addition(no1,no2)
    print("Addition : ",res)

