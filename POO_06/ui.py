from cliente import Cliente
from clientedao import ClienteDAO

class UI:
    def main():
        op = 0
        while op != 9:
            op = UI.menu()
            if op == 1: UI.inserir()
            if op == 2: UI.listar()
            if op == 3: UI.atualizar()
            if op == 4: UI.excluir()
    def menu():
        print("1 - Inserir, 2 - Listar, 3 - Atualizar, 4 - Excluir, 9 - Fim")
        return int(input("Informe a opção: "))
    def inserir():
        #id = int(input("Informe o id: "))
        nome = input("Informe o nome: ")
        c = Cliente(0, nome)
        ClienteDAO().inserir(c)
    def listar():
        for c in ClienteDAO().listar():
            print(c)
    def atualizar():
    def excluir()            

UI.main()