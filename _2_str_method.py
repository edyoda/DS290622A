# # class test:
# #     def __str__(self):
# #         return "Hello Bharati!"

# # obj = test()
# # print(obj)

# # # whenever you print the object of the class, then bydefault __str__() method gets called

# # class laptop:

# #     def __init__(self,__processor,brand,harddisk):
# #         self.__processor = __processor
# #         self.brand = brand
# #         self.hardisk = harddisk
    
# #     def __str__(self):
# #         return f"Laptop details : \n Processor: {self.__processor} \n Brand : {self.brand} \n Harddisk : {self.hardisk} "

# #     def set_processor(self,processor):
# #         self.__processor = processor

# #     def get_processor(self):
# #         return self.__processor

# #     def set_brand(self,brand):
# #         self.brand = brand

# #     def get_brand(self):
# #         return self.brand

# #     def set_harddisk(self,harddisk):
# #         self.harddisk = harddisk

# #     def get_harddisk(self):
# #         return self.harddisk
    
# # Laptop = laptop ("I9 Processor","Dell","Seagate SSD512gb")
# # print(Laptop)

# # print()

# # Laptop.set_processor("I7 Processor")
# # print(Laptop.get_processor())

# # Laptop.set_brand("Lenova")
# # print(Laptop.get_brand())

# # Laptop.set_harddisk("Transand SSD256 gb")
# # print(Laptop.get_harddisk())


# class laptop:
#     def __init__(self,brand,model,price):
#         self.__brand=brand
#         self.model=model
#         self.price=price

#     def __str__(self):
#         return f'Laptop Brand: {self.__brand}\nLaptop model: {self.model}\nLaptop price:{self.price}'

#     def set_brand(self,brand):
#         self.__brand=brand
#     def get_brand(self):
#         return self.__brand
#     def set_model(self,model):
#         self.model=model
#     def get_model(self):
#         return self.model
#     def set_price(self,price):
#         self.price=price
#     def get_price(self):
#         return self.price

# lap=laptop('HP','B6',50000)
# print(lap)
# print(lap.get_brand())
# lap.set_brand("Lenovo")
# print(lap)

class laptop:
    def __init__(self,brand,ram,processor):
        self.brand=brand
        self.ram=ram
        self.processor=processor
    
    def __str__(self):
        return f"SPECS:\n brand :{self.brand}\n RAM :{self.ram}\n processor :{self.processor}"
    
    def set_brand(self,brand):
        self.brand= brand
    def set_ram(self,ram):
        self.ram=ram
    def set_processor(self,processor):
        self.processor=processor
    
    def get_brand(self):
        return self.brand
    def get_ram(self):
        return self.ram
    def get_processor(self):
        return self.processor
    
lap1=laptop('apple','8gb','i7')

print(lap1)


lap1.set_brand('dell')
lap1.set_ram('4GB')
lap1.set_processor("i5")


print(lap1.get_brand())
print(lap1.get_ram())
print(lap1.get_processor()) 

