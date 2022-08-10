class Dad:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def display(self):
        return f"Name : {self.name} , Age : {self.age}" 

class Son(Dad):
    def __init__(self,name,age,occupation):
        super().__init__(name,age)
        self.occupation = occupation
        
    def occupation_method(self):
        print(self.occupation)

son = Son("Ram",45,"Student")
data = son.display()
print(data)

son.occupation_method()

