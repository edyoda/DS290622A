# Hybrid Inheritance 
# It's a combination of all the types of inheritance

class A:
    def a(self):
        print("a")

class B(A):
    def b(self):
        print("b")

class C(A):
    def c(self):
        print("c")

class D(C):
    def d(self):
        print("d")

    def data(self):
        print("first")    

class E(C):
    def e(self):
        print("e")
    def data(self):
        print("second")    

class F(D,E):
    def f(self):
        print("f")
        
obj=B()
obj.a()

obj1=C()
obj1.a()

obj2=D()
obj2.c()
obj2.a()

obj3=E()
obj3.c()
obj3.a()

obj4=F()
obj4.d()
obj4.e()
obj4.data()
