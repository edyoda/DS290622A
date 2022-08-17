class InvalidAgeError(Exception):
    # def __str__(self):
    #     return "You are still a kid!"

    def __init__(self):
        print("You are still a kid!")