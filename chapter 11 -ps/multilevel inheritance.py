class employee:
    a = 1
    b = 3
class programing(employee):
    b = 2

class jit(programing):
    c = 3

obj = jit()
jana = programing()
kobita = employee()
print(obj.a, obj.b, obj.c)
print(jana.a, jana.b)
print(kobita.a, kobita.b)