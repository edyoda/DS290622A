# finally block - the code within finally block gets executed regardless of whether 
# we got an exception or not

# try:
#     div = 10/5
#     print("Division : ",div)
# except Exception as ex:
#     print(ex)
# finally:
#     print("Final Block")


file = open("demo.txt","w")
try:
    file.write("Hey!")
except:
    pass
finally:
    print("In Finally")
    file.close()

