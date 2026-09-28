class emlpoyee:
    language = "python" # this is class attribute
    saalary = 12000


    def getinfo(self):
        print(f"the language is{self.language}. the salary is {self.saalary}")

    def greet(self):
        print("good night")


jit = emlpoyee()
jit.language = "java"  # this is an instance attribute
jit.greet()

jit.getinfo()
