class employee:
    language = "python" 
    salary = 100000

    def __init__(self, name, salary, language):
        

        self.name = name
        self.salary = salary
        self.language = language
        print("created the objected this ")
    def gretinfo(self):
        print(f"jit is language programing{self.language}. and salary company{self.salary}")

    @staticmethod

    def greet():
        print("good morning jit jana")

jit = employee("jana", 1300000, "javascript")

print(jit.name, jit.salary, jit.language)

jit.greet()

    
