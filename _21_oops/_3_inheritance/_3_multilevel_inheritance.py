class grandpa:
    def field(self):
        print("Field")

class dad(grandpa):
    def flat(self):
        print("Flat")

    def bike(self):
        print("Bike")

class son(dad):
    def mobile(self):
        print("Mobile")

obj = son()
obj.mobile()
obj.flat()
obj.bike()
obj.field()