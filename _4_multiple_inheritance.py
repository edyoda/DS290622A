# Multiple Inheritance
# Multiple Parent classes and single child class

class c_lang:
    def procedural_feature(self):
        print("Procedural Feature")

    def language(self):
        print("C Language")

class cpp_lang:
    def oops_feature(self):
        print("OPPs Feature")

    def language(self):
        print("Cpp Language")

class python(cpp_lang,c_lang):
    def both_feature(self):
        print("Both Procedural and OPPs Feature")

    def language(self):
        print("Python Language")

obj = python()
obj.procedural_feature()
obj.oops_feature()
obj.both_feature()
obj.language()


print(python.__mro__) # Method Resolution Order
print(python.mro())

