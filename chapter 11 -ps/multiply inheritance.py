class employee:
    company = "google"

    def jit(self):
        print(f"company name is {self.company}. and language is {self.language}. and salary is {self.salary}")


class coder:
    language = "python"

    def coder_info(self):
        print(f"company name is {self.company}. and language is {self.language}")


class programmer(employee, coder):
    def show(self):
        print(f"company name is {self.company}. and language is {self.language}")


a = programmer()
b = employee()
c = coder()

print(a.company, b.company, c.language)
#print(b.company)
#print(c.language)