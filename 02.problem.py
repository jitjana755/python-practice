class calculater:
    def __init__(self, n):
        self.n = n
        
        
    def square(self):
        print(f"the square {self.n*self.n}")
    def cub(self):
            print(f"the cub {self.n*self.n}")
    def squarroot(self):
            print(f"the squareroot{self.n**1/2}")

a = calculater(4)
a.square()
a.cub()
a.squarroot()
