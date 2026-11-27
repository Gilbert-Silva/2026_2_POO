#x = int(input())
#print(x)

#x = [1, 5, 8, 0]
#print(x[10])

#x = {"RN" : "Natal"}
#print(x["PB"])  # raise KeyError('PB')

try:
    a = int(input("Digite um número: "))
    b = int(input("Digite outro número: "))
    print(a/b)
except Exception as erro:
    print("Todos os valores devem ser números inteiros, segundo valor não pode ser zero")
    print(erro)
    print(type(erro))
print("Olá")