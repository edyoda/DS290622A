# Hierarchical Inheritance
# Single Parent and multiple child classes

class Country:
    def region(self):
        print("Region")

class India(Country):
    def language(self):
        print("Hindi")

class USA(Country):
    def language(self):
        print("English")

obj = India()
obj.region()
obj.language()

obj1 = USA()
obj1.region()
obj1.language()



