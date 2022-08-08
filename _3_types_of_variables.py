# local variable
# global variable


# instance variable
# are those variable which are define inside the methods/constructor
# it is created by using self keyword as prefix ex. self.<variable_name>
# scope : throughout the class
# different memory is provided for different instance variable
# instance variable can be called using object name


# static/class variable 
#   - this variable is declared inside the class and outside the method/constructor
#   - scope is throughout the class
#   - class variable can be accessed using class name
#   - syntax to call it : <class_name>.<class_variable_name>
#   - it is used for memory management
#   - as is shares the same memory
#   - class variable can be called using class name/object name

class school:

    school_name = "Coder"                  #class/static variable
    
    def __init__(self,name,rno):
        self.name = name
        self.rno = rno

    def display(self):
        print(f"Hi {self.name} from {school.school_name}, your rno is {self.rno}!")

print(school.school_name)
obj = school("Bharati",24)
obj.display()
print(obj.school_name)

# school.school_name = "Edyoda"
obj1 = school("Leena",24)
obj1.display()
print(obj1.school_name)

obj2 = school("Rajkumar",22)
obj2.display()
print(obj2.school_name)

print(obj1.name)
