class programer:
    comapy = "wipro"

    def __init__(self, name, salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin
    @staticmethod
    def geet():
        print("jit is backend devloper")
p = programer("jit", 120000, 721625)
print(p.name, p.salary, p.pin)
p.geet()



        