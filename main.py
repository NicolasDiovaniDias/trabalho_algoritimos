#from Desktop import Desktop
#
#Produto1 = Desktop('carro', "amarelo", 19, "preto", 200)
#Produto1.cadastrar()
#Produto1.getinfo()
import sys
from PyQt5.QtWidgets import *
from TelaDesktop import TelaDesktop
from TelaNotebook import TelaNotebook
app = QApplication(sys.argv)
telaDesktop = TelaDesktop()
telaDesktop.show()
telaNotebook = TelaNotebook()
telaNotebook.show()
sys.exit(app.exec_())