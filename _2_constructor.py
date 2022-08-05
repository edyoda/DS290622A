# constructor 
# it a function with same as class name
# it is defined using __init__()
# you need not have to call it explicitly, it automatically gets called while creating object
# it is used to create object
# it is used to initialise instance variable

#! Note : It's highly recommended not to write print statements or logic inside the constructors

# Types of Constructor
# 1. Default Constructor - are constructors which are provided by compiler, when you have not created constructor in your class
# 2. Zero Constructor - constructor without any parameter
# 3. Parameterized Constructor - constructor with parameters


class constructor:
    def __init__(self,name,rno):                   # Constructor # Parameterized Constructor
        self.name = name
        self.rno = rno
        
    def display(self):
        print(f"Name : {self.name} , Rno : {self.rno}")

obj = constructor("Bharati",24) # __init__()
obj.display()

obj1 = constructor("Deepak",25)
obj1.display()


# class constructor:
#     def __init__(self):                   # Constructor  # Zero Constructor
#         print("Constructor")

    

# obj1 = constructor() 
# obj2 = constructor() 
# obj3 = constructor() 
