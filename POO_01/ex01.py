class Triangulo:
    def __init__(self):
        self.b = 0
        self.h = 0
    def calcular_area(self):
        return self.b * self.h / 2
    
x = Triangulo()    # Triangulo.__init__(x)  
print(x.b, x.h) 
x.b = -10
x.h = 20
print(x.b, x.h) 
print(x.calcular_area()) 

y = Triangulo()
y.b = 30
y.h = 40
print(y.calcular_area()) 
print(x)
print(y)

z = x
z.b = 50
print(x.b)


        