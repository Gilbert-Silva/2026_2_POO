import json
from cliente import Cliente

class ClienteDAO:
    def __init__(self):
        self.__arquivo = "clientes.json"
        self.__objetos = []
    def inserir(self, obj):
        self.__abrir()
        self.__objetos.append(obj)
        self.__salvar()
    def listar(self):
        self.__abrir()
        return self.__objetos
    def __abrir(self):
        self.__objetos = []
        arquivo = open(self.__arquivo, mode="r")
        objetos_json = json.load(arquivo)      # lista de dicionários
        for obj in objetos_json:               # cada objeto é um dicionário  
            self.__objetos.append(Cliente(obj["id"], obj["nome"]))
        arquivo.close()
    def __salvar(self):
        arquivo = open(self.__arquivo, mode="w")
        json.dump(self.__objetos, arquivo, default = vars)
        arquivo.close()
        