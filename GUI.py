 

import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow,QApplication, QPushButton


class mainGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        #self.setWindowTitle("Automata")
        self.setFixedSize(900,700)
        
        uic.loadUi('guiApp.ui',self)
        self.botones()

    def botones(self):
        self.botonAutenticar.clicked.connect(self.autenticar)
    
    def autenticar(self):
        sender = self.sender()
        texto=self.textoAutenticar.text()
        self.statusBar().showMessage(sender.text() + texto)

   


if __name__ == '__main__':
    app=QApplication(sys.argv)
    GUI=mainGUI()
    GUI.show()
    sys.exit(app.exec_())
