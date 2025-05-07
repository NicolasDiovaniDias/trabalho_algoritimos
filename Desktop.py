from Produto import Produto
class Desktop(Produto):
    def __init__(self, modelo, cor, preco, categoria, _potenciaDaFonte):
        super().__init__(modelo, cor, preco, categoria)
        self._potenciaDaFonte = _potenciaDaFonte

    def __str__(self):
        return super().__str__()+"\nPotencia da Fonte = "+str(self._potenciaDaFonte)
    
    def getinfo(self):
         return super().getinfo()
    
    def get_potenciaDaFonte(self):
        return self._potenciaDaFonte

    def set_potenciaDaFonte(self,_potenciaDaFonte):
        self._potenciaDaFonte = _potenciaDaFonte


    def cadastrar(self):
         print(f"Produto cadastrado com sucesso!{self.modelo}")
