# def outer():
#     print("Outer Function")
#     def inner():
#         print("Inner Function")
#     inner()

# outer()

def info():
    print("Suraj")
    global rno
    def rno():
        print("24")
info()
rno()
