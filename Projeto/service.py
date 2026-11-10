from models.cliente import Cliente
from models.clientedao import ClienteDAO

class Service:
    @staticmethod
    def cliente_inserir(nome, email, fone):
        c = Cliente(0, nome, email, fone)
        ClienteDAO().inserir(c)
    @staticmethod
    def cliente_listar():
        return ClienteDAO().listar()
    @staticmethod
    def cliente_listar_id(id):
        return ClienteDAO().listar_id(id)
    @staticmethod
    def cliente_atualizar(id, nome, email, fone):
        c = Cliente(id, nome, email, fone)
        ClienteDAO().atualizar(c)        
    @staticmethod
    def cliente_excluir(id):
        ClienteDAO().excluir(id)        

    

