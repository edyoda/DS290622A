# Abstraction 
# hiding implementation and showing functionality

# abstact class 
# - a class with atleast one abstract method
# - we cannot create an object of abstract class
# - we can also have normal/instance methods in abstract class

# abstract method
# - methods without body
# - with decorator "abstractmethod"

from abc import ABC,abstractmethod

class Laptop(ABC):                    # abstract class

    @abstractmethod
    def processor(self):
        pass



class Programmer(Laptop):

    def processor(self):
        print("It's processing things!")

# laptop = Laptop()
# laptop.processor()

programmer = Programmer()
programmer.processor()