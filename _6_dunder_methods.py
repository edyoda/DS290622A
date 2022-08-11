# Dunder Method | Special Method | Magic Method

# __init__
# __str__
# __mro__

print(dir(list))

no1 = 10
no2 = 20
add = no1 + no2
print(add)

class special_method:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        
    def __repr__(self):
        return "Hey"

    def __add__(self,another):
        return self.name + another.name # obj1.salary + obj2.salary

    def __mul__(self,another):
        return self.salary * another.salary

    def __len__(self):
        return len(self.name)

obj1 = special_method("Ram",10000)
obj2 = special_method("Laxman",15000)

print(obj1.name)

print(obj1 + obj2)

print(obj1 * obj2)

print(len(obj2))
    
        
