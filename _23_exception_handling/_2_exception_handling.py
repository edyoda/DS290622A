class exception:
    def division(self):
        no1 = int(input("Enter no1 : "))
        no2 = int(input("Enter no2 : "))
        div = no1/no2
        print("Divison : ",div)
        print("End of program")

    def divide(self):
        self.division()

obj = exception()
obj.divide()

# division()
# divide()
# main()