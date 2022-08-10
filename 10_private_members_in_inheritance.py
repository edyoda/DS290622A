# If there is some parent class data which you don't want your child class to have access to,
# then we can make it private and restrict it's access. 

# we can make variable and method both as private by just adding ' __ ' before it.

class Dad:
    def __init__(self,bike,flat,fd):
        self.bike = bike
        self.flat = flat
        self.__fd = fd

    def __car(self):
        print("Car")

class Son(Dad):
    pass

son = Son("honda","3BHK",100000)
print(son.bike)
print(son.flat)
# print(son.__fd)

son.__car()