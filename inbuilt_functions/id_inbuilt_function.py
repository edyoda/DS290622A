no = 10
name = "Bharati"
price = 10.9
human = True


print(id(no))
print(id(name))
print(id(price))
print(id(human))

# id function is used to retreive the unique ID of the object
# unique ID gets created once the object is created
# every object has a unique id
# the id is the object's memory address and will be different for each time you run the program,
# except for some objects i.e -5 to 256, as this objects are already present in the memory.

no1 = 300
no2 = 300	
print(id(no1))
print(id(no2))


no1 = 10
print(id(no1))

no1 = 20
print(id(no1))

bool_demo = 1+5j
print(id(bool_demo))
	
bool_demo = 2+5j
print(id(bool_demo))
