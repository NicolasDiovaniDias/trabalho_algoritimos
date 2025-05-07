from Produto import Produto
class Notebook(Produto):
    def __init__(self, modelo, cor, preco, categoria, _tempoDeBateria):
        super().__init__(modelo, cor, preco, categoria)
        self._tempoDeBateria = _tempoDeBateria

    def __str__(self):
        return super().__str__()+"\nTempo de Bateria = "+str(self._tempoDeBateria)

    def getinfo(self):
         return super().getinfo()

    def get_tempoDeBateria(self):
        return self._tempoDeBateria

    def set_tempoDeBateria(self,_tempoDeBateria):
        self._tempoDeBateria = _tempoDeBateria

    def cadastrar(self):
         print(f"Produto cadastrado com sucesso!{self.modelo}")