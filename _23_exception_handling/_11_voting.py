from _12_customize_exception import InvalidAgeError

class Vote:
    def vote(self,age):
        try:
            if age >= 18:
                print("Successfully Voted")
            else:
                raise InvalidAgeError()
        except Exception as ex:
            print(ex)
            
obj = Vote()
obj.vote(6)
