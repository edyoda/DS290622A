class Method:

    def __init__(self,name) -> None:
        self.name = name

    @staticmethod
    def static_method():
        return "Hey All"


method = Method("Bharati")
print(method.static_method())