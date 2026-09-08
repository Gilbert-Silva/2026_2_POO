class Triangulo:
    def __init__(self, b, h):
        self.b = b
        self.h = h
    def __str__(self):
        return f"Olá, eu sou um triângulo, minha base é {self.b}, minha altura é {self.h}"

x = Triangulo(10, 20)
print(x)
x.b = 50
print(x.b, x.h)
x = 0 # objetos saem da memória qdo não há mais referências para ele
print(Triangulo(30, 40))
