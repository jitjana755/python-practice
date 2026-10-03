class employee:
    company = "google"
    def show(self):
        print(f"company name is {self.company}. aand language is {self.language}. and {self.salary}")

class programmer:
    company = "microsoft"
    def function(self):
        print(f"company name is {self.company}. aand language is {self.language}. and {self.salary}")
class data:
    company = "facebook"
    language = "Python"
    salary = 50000

    def display(self):
        print(f"company name is {self.company}. aand language is {self.language}. and {self.salary}")

p = employee()
p1 = programmer()
p2 = data()
print(p.company, p1.company, p2.company)