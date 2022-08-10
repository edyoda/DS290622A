# Polymorphism
# poly - many
# morphism - form
# single entity, many forms

# types of polymorphism
# 1. compile time polymorphism (overloading) - this is not supported in python
# 2. runtime polymorphism (overriding)

# 1. compile time polymorphism (overloading)
# Overloading - same name method with different parameters (seq,datatype,no. of parameter)

# class human:
#     def behaviour(self,friends):
#         print("Masti")

#     def behaviour(self,family,home):
#         print("Sajjan!")

# obj = human()
# obj.behaviour("Pranali")



# 2. runtime polymorphism (overriding)

# Overriding 
# - overriding can only be done in inheritance
# - if parent class method implementation is not according to what we want, 
#   then we can override and write our own implementation

# when a class is not inheriting any class, then bydefault it inherits "object" class
# __str__() is object class method which returns memory address of the object
# but as we don't want memory address, we override __str__() and modify it's implementation

# rules of overriding
# 1. parent class method name and child class method name should be same
# 2. no. of parameters in child class method should be exact same with parent class method

class old_tv:
    def color(self):
        print("b/w")

    def video(self):
        print("480p")

class modern_tv(old_tv):
    def color(self):              # override 
        print("colored tv")

    def additional_feature(self):
        print("smart tv")

obj = modern_tv()
obj.color()







