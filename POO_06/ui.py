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
        email = input("Informe o e-mail: ")
        fone = input("Informe o fone: ")
        c = Cliente(0, nome, email, fone)
        ClienteDAO().inserir(c)
    def listar():
        for c in ClienteDAO().listar():
            print(c)
    def atualizar():
        UI.listar()
        id = int(input("Informe o id a ser atualizado: "))
        nome = input("Informe o novo nome: ")
        email = input("Informe o novo e-mail: ")
        fone = input("Informe o novo fone: ")
        c = Cliente(id, nome, email, fone)
        ClienteDAO().atualizar(c)        
    def excluir():            
        UI.listar()
        id = int(input("Informe o id a ser excluído: "))
        ClienteDAO().excluir(id)        

UI.main()