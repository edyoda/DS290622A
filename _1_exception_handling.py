# Exception - an unwanted/unexpected event
# Handling  - not fixing it but finding an alternate way to gracefully complete the flow

# Blocks
# try block    - it is use to store the suspicious code
# except block - it is use to handle the exception


# class exception:
#     def division(self):
#         no1 = int(input("Enter no1 : "))
#         no2 = int(input("Enter no2 : "))
#         div = no1/no2
#         print("Divison : ",div)
#         print("End of program")

# obj = exception()
# obj.division()


class exception:
    def division(self):
        no1 = int(input("Enter no1 : "))
        no2 = int(input("Enter no2 : "))
        div = 0
        
        try:
            div = no1/no2
        except Exception as ex:
            print(ex)

        print("Divison : ",div)
        print("End of program")

obj = exception()
obj.division()

