class exception:
    def division(self):
        no1 = 0
        no2 = 0
        div = 0
        
        try:
            no1 = int(input("Enter no1 : "))
            no2 = int(input("Enter no2 : "))
            div = no1/no2
        except:
            pass

        print("Divison : ",div)
        print("End of program")

obj = exception()
obj.division()

# ValueError: invalid literal for int() with base 10: 'Bharati'
