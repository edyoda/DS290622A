# # class - is the blueprint (planning)
# # object - it is the instance of the class
# # methods 
# #   - are functions which are define inside the class
# #   - every function defined inside the class must have self keyword as a parameter

# # in python, while calling method, object is understood as argument, hence we need to pass self

# # self
# #    - self is a keyword
# #    - it represents object of the class

# # syntax 
# # class <class_name>:
# #    class_body


# instance variable
# are those variable which are define inside the methods/constructor
# it is created by using self keyword as prefix ex. self.<variable_name>
# scope : throughout the class
# different memory is provided for different instance variable
# instance variable can be called using object name

class building:              # class is created

    def bricks(self,no_of_bricks=9000):
        print(f"{no_of_bricks} bricks!")

    def door(self):
        self.no_of_doors = 10  # instance variable
        return f"{10} doors"

    def window(self):
        print(self.no_of_doors)
        print("40 windows")

obj = building()   # object is created #syntax: <class_name>() # it is a default constructor
obj.bricks()
data = obj.door()
print(data)
obj.window()

# if you don't create a constructor in your class, then compiler provides the default 
# constructor 




# class calculator:        #Class created

#     def add(self,no1,no2):  #methods
#         return no1+no2
#     def sub(self,no1,no2):
#         return no1-no2
#     def mult(self,no1,no2):
#         return no1*no2
#     def div(self,no1,no2):
#         return no1//no2
        
# obj_calc = calculator()  #Object created

# no1 = int(input("Enter 1st number: "))
# no2 = int(input("Enter 2st number: "))

# data = obj_calc.add(no1,no2)
# print(data)
# data = obj_calc.sub(no1,no2)
# print(data)
# data = obj_calc.mult(no1,no2)
# print(data)
# data = obj_calc.div(no1,no2)
# print(data)
