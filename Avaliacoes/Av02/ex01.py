from datetime import datetime, timedelta

class Atleta:
    def __init__(self, i, n):
        self.set_id(i)
        self.set_nome(n)
    def set_id(self, i):
        if i < 0: raise ValueError("Id deve ser positivo")
        self.__id = i
    def get_id(self):
        return self.__id
    def set_nome(self, n):
        if n == "": raise ValueError("Nome deve ser informado")
        self.__nome = n
    def get_nome(self):
        return self.__nome
    def __str__(self):
        return f"{self.__id} - {self.__nome}"
    
class Treino:
    def __init__(self, i, i_a, dt, ds, t):
        self.set_id(i)
        self.set_id_atleta(i_a)
        self.set_data(dt)
        self.set_distancia(ds)
        self.set_tempo(t)
    def set_id(self, i):
        if i < 0: raise ValueError("Id deve ser positivo")
        self.__id = i
    def get_id(self):
        return self.__id
    def set_id_atleta(self, i_a):
        if i_a < 0: raise ValueError("Id deve ser positivo")
        self.__id_atleta = i_a
    def get_id_atleta(self):
        return self.__id_atleta
    def set_data(self, dt):
        if dt > datetime.now(): raise ValueError("Data deve estar no presente ou passado")
        self.__data = dt
    def get_data(self):
        return self.__data
    def set_distancia(self, ds):
        if ds < 0: raise ValueError("Distância deve ser positiva")
        self.__distancia = ds
    def get_distancia(self):
        return self.__distancia
    def set_tempo(self, t):
        if t < timedelta(0): raise ValueError("Tempo deve ser positivo")
        self.__tempo = t
    def get_tempo(self):
        return self.__tempo
    def pace(self):
        return self.__tempo / self.__distancia
    def __str__(self):
        return f"{self.__id} - {self.__id_atleta} - {self.__data} - {self.__distancia} - {self.__tempo} - {self.pace()}"

class UI:
    __atletas = []
    __treinos = []
    @staticmethod
    def main():
        op = 0
        while op != 9:
            op = UI.menu()
            if op == 1: UI.inserir_atleta()
            if op == 2: UI.listar_atletas()
            if op == 3: UI.inserir_treino()
            if op == 4: UI.listar_treinos()
            if op == 5: UI.atleta_mais_rapido()
    @staticmethod
    def menu():
        print("1-Inserir Atleta  2-Listar Atletas  3-Inserir Treino  4-Listar Treinos  5-Mais Rápido  9-Fim")
        return int(input("Informe uma opção: "))
    @classmethod
    def inserir_atleta(cls):
        id = int(input("Informe o id: "))
        nome = input("Informe o nome: ")
        x = Atleta(id, nome)
        cls.__atletas.append(x)
    @classmethod
    def listar_atletas(cls):
        for x in cls.__atletas: print(x)
    @classmethod
    def inserir_treino(cls):
        id = int(input("Informe o id: "))
        cls.listar_atletas()
        id_atleta = int(input("Informe o id do atleta: "))
        data_str = input("Informe a data dd/mm/aaaa: ")
        data = datetime.strptime(data_str, "%d/%m/%Y")
        distancia = float(input("Informe a distância em km: "))
        tempo_str = input("Informe o tempo MM:SS: ")
        min, seg = map(int, tempo_str.split(":"))
        tempo = timedelta(minutes=min, seconds=seg)
        x = Treino(id, id_atleta, data, distancia, tempo)
        cls.__treinos.append(x)
    @classmethod
    def listar_treinos(cls):
        for x in cls.__treinos: print(x)
    @classmethod
    def atleta_mais_rapido(cls):
        treino = min(cls.__treinos, key = lambda x : x.pace())
        for x in cls.__atletas:
            if x.get_id() == treino.get_id_atleta(): 
                print(x)

#UI.main()

x = Atleta(1, "Eduardo")

x._Atleta__id = -1
print(x._Atleta__id)
print(x._Atleta__nome)
