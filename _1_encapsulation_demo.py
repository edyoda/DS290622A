# Encapsulation
#  - it is used to bind attributes(variables) and behaviour(methods) together into single unit
#  - to access private member through public environment

# private member - cannot be accessed outside the class

class Car:
    
    def __init__(self,__engine,brand,mileage):
        self.__engine = __engine               # private member
        self.brand  = brand
        self.mileage = mileage

    def __str__(self):
        return f"Car Details : \nEngine : {self.__engine} \nBrand : {self.brand} \nMileage : {self.mileage}"

    # setter
    def set_engine(self,engine):               # public environment
        self.__engine = engine

    # getter
    def get_engine(self):
        return self.__engine

    def set_brand(self,brand):
        self.brand = brand

    def get_brand(self):
        return self.brand

    def set_mileage(self,mileage):
        self.mileage = mileage

    def get_mileage(self):
        return self.mileage

car = Car("Diesel Engine","BMW","35km per litre")
print(car)

print()

car.set_engine("Petrol Engine!!!")
print(car.get_engine())

car.set_brand("Audi!!!")
print(car.get_brand())

car.set_mileage("40km/l")
print(car.get_mileage())