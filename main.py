import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow,QApplication, QPushButton

class Automata():
    def __init__(self):
        self.estado=0
        self.numero=0
        self.cont=0
        mensaje=""

    def q0(self,letras):
        self.estado = 0
        if (self.numero != 0 and letras[self.cont] == 'b'):
            self.numero = self.numero - 1
            self.cont = self.cont+1
            self.q1(letras)
        elif(self.numero == 0):
            self.compilador()
        else:
            print("Error de escritura")

    def q1(self,letras):
        self.estado = 1
        if (self.numero != 0 and letras[self.cont] == 'b'):
            self.numero = self.numero - 1
            self.cont = self.cont + 1
            self.q2(letras)
        elif (self.numero != 0 and letras[self.cont] == 'a'):
            self.numero = self.numero - 1
            self.cont = self.cont + 1
            self.q3(letras)
        elif (self.numero == 0):
            self.compilador()
        else:
            print("Error de escritura")

    def q2(self,letras):
        self.estado = 2
        if (self.numero != 0 and letras[self.cont] == 'a'):
            self.numero = self.numero - 1
            self.cont = self.cont + 1
            self.q5(letras)
        elif (self.numero != 0 and letras[self.cont] == 'b'):
            self.numero = self.numero - 1
            self.cont = self.cont + 1
            self.q4(letras)
        elif (self.numero == 0):
            self.compilador()
        else:
            print("Error de escritura")

    def q3(self,letras):
        self.estado = 3
        if (self.numero != 0 and letras[self.cont] == 'a'):
            self.numero = self.numero - 1
            self.cont = self.cont + 1
            self.q6(letras)
        elif (self.numero == 0):
            self.compilador()
        else:
            print("Error de escritura")

    def q4(self,letras):
        self.estado = 4
        if (self.numero != 0 and letras[self.cont] == 'a'):
            self.numero = self.numero - 1
            self.cont = self.cont + 1
            self.q3(letras)
        elif (self.numero != 0 and letras[self.cont] == 'b'):
            self.numero = self.numero - 1
            self.cont = self.cont + 1
            self.q4(letras)
        elif (self.numero == 0):
            self.compilador()
        else:
            print("Error de escritura")

    def q5(self,letras):
        self.estado = 5
        if (self.numero != 0 and letras[self.cont] == 'a'):
            self.numero = self.numero - 1
            self.cont = self.cont + 1
            self.q6(letras)
        elif (self.numero != 0 and letras[self.cont] == 'b'):
            self.numero = self.numero - 1
            self.cont = self.cont + 1
            self.q7(letras)
        elif (self.numero == 0):
            self.compilador()
        else:
            print("Error de escritura")

    def q6(self,letras):
        self.estado = 6
        if (self.numero != 0 and letras[self.cont] == 'a'):
            self.numero = self.numero - 1
            self.cont = self.cont + 1
            self.q3(letras)
        elif (self.numero != 0 and letras[self.cont] == 'b'):
            self.numero = self.numero - 1
            self.cont = self.cont + 1
            self.q4(letras)
        elif (self.numero == 0):
            self.compilador()
        else:
            print("Error de escritura")

    def q7(self,letras):
        self.estado = 7
        if (self.numero != 0 and letras[self.cont] == 'a'):
            self.numero = self.numero - 1
            self.cont = self.cont + 1
            self.q8(letras)
        elif (self.numero == 0):
            self.compilador()
        else:
            print("Error de escritura")

    def q8(self,letras):
        self.estado = 8
        if (self.numero != 0 and letras[self.cont] == 'b'):
            self.numero = self.numero - 1
            self.cont = self.cont + 1
            self.q7(letras)
        elif (self.numero == 0):
            self.compilador()
        else:
            print("Error de escritura")

    def compilador(self):
        if(self.estado == 3):
            self.mensaje="Error, no se llega a un estado valido"
            #automata.statusBar().showMessage("Error, no se llega a un estado valido")
            print("Error, no se llega a un estado valido")
        else:
            self.mensaje="Valor correcto"
            #automata.statusBar().showMessage("Valor correcto")
            print("Valor correcto")

    def recorido(self, palabra):
        lis=list(palabra)
        self.numero=len(lis)
        self.cont=0
        self.q0(lis)
        return self.mensaje




auto=Automata()
auto.recorido("bbbaabaaaabbaa")


