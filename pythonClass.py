#_{className}__variableName => this is a private variable in Python
class CustomClass:
    def __init__(self, name):
        self.__name = name  # Private variable

    def get_name(self):
        return self.__name  # Accessing the private variable
    

inputName = input("Enter your name: ")
name = CustomClass(inputName)
print(f"Your output name is {name.get_name()}")  # Output: Rohaan