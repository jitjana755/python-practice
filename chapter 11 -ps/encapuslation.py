class Student:

    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def show(self):
        print("Name:", self.name)
        print("Age:", self.__age)


s = Student("Jit", 20)

s.show()