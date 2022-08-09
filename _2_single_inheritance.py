# Single Inheritance
# single parent class and single child class

class Dad:                   # Parent Class
    def flat(self):
        print("Flat")

    def car(self):
        print("Car")

    def bike(self):
        print("Dad's Bike")

class Son(Dad):   # Son class has inherited Dad class     # Child Class
    def bike(self):
        super().bike()
        print("Son's Bike")

    def mobile(self):
        print("Mobile")

son = Son()
son.bike()
son.mobile()
son.car()
son.flat()

# self keyword - represents object of current class
# super keyword - which represents object of immediate parent class