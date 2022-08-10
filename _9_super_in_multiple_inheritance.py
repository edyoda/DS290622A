# Multiple Inheritance
# Multiple Parent classes and single child class

class c_lang:
    def __init__(self):
        print("C")

    def procedural_feature(self):
        print("Procedural Feature")

    def language(self):
        print("C Language")

class cpp_lang:
    def __init__(self):
        print("C++")

    def oops_feature(self):
        print("OPPs Feature")

    def language(self):
        print("Cpp Language")

class python(cpp_lang,c_lang):
    def __init__(self):
        cpp_lang.__init__(self)
        c_lang.__init__(self)
        print("Python")

    def both_feature(self):
        print("Both Procedural and OPPs Feature")

    def language(self):
        cpp_lang.language(self)
        c_lang.language(self)
        print("Python Language")

obj = python()
obj.procedural_feature()
obj.oops_feature()
obj.both_feature()
obj.language()




