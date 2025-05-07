from abc import ABC, abstractmethod
class Produto(ABC):
    def __init__(self, modelo, cor, preco, categoria):
        self.modelo =  modelo
        self.cor = cor
        self.preco = preco
        self.categoria = categoria
    def __str__(self):
        return (f"modelo = {self.modelo}\ncor = {self.cor}\npreco = {self.preco}\ncategoria = {self.categoria}")
    def getinfo(self):
        print(self)
    @abstractmethod
    def cadastrar(self):
        pass
