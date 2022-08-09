class A:
    def a(self):
        print("a")
class B:
    def b(self):
        print("b")

class C(A,B):
    def c(self):
        print("c")

class D(C,B):
    def d(self):
        print("d")

class E(D,A):     # A,D will give "TypeError: Cannot create a consistent method resolution"
    def e(self):
        print("e")



obj = C()
obj.a()
obj.b()
obj.c()

obj1 = D()
obj1.a()
obj1.b()
obj1.c()
obj1.d()

obj2 = E()
obj2.a()
obj2.b()
obj2.c()
obj2.d()
obj2.e()

print(E.__mro__)
print(D.mro())
print(C.mro())
print(B.mro())
