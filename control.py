#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
import sys, time, serial

from ventanaControlArduino import Ui_Form

class Myform(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.ui=Ui_Form()
        self.ui.setupUi(self)

        self.estado = [0,0,0,0]

        self.arduino = serial.Serial('/dev/ttyACM0', 9600)

        """cant=int(self.arduino.readline())
        for i in range(cant):
            txtDelArduino = self.arduino.readline()
            txt = txtDelArduino
            self.ui.txtArduino.append(txt)"""

    def arduinoDice(self):
        if (self.arduino.inWaiting()>0):
            txtDelArduino = self.arduino.readline()
            txt= "Arduino> " +txtDelArduino
            self.ui.txtArduino.append(txt)
        else:
            self.ui.txtArduino.append("---")

    def rele4(self):
        if self.estado[3]==0:
            self.estado[3]=1
            self.ui.btnRel4.setText("Apagar Rele 4")

            self.arduino.write('R') #para el relé 4, los char up son: QWER
            self.arduinoDice()            

        else:
            self.estado[3] = 0
            self.ui.btnRel4.setText("Encender Rele 4")

            self.arduino.write('F') #para el relé 4, los char down son: ASDF
            self.arduinoDice()

    def rele3(self):
        if self.estado[2]==0:
            self.estado[2]=1
            self.ui.btnRel3.setText("Apagar Rele 3")

            self.arduino.write('E') #para el relé 4, los char up son: QWER
            self.arduinoDice()
        else:
            self.estado[2] = 0
            self.ui.btnRel3.setText("Encender Rele 3")

            self.arduino.write('D') #para el relé 4, los char down son: ASDF
            self.arduinoDice()

    def rele2(self):
        if self.estado[1]==0:
            self.estado[1]=1
            self.ui.btnRel2.setText("Apagar Rele 2")

            self.arduino.write('W') #para el relé 4, los char up son: QWER
            self.arduinoDice()
        else:
            self.estado[1] = 0
            self.ui.btnRel2.setText("Encender Rele 2")

            self.arduino.write('S') #para el relé 4, los char down son: ASDF
            self.arduinoDice()


    def rele1(self):
        if self.estado[0]==0:
            self.estado[0]=1
            self.ui.btnRel1.setText("Apagar Rele 1")

            self.arduino.write('Q') #para el relé 4, los char up son: QWER
            self.arduinoDice()
        else:
            self.estado[0] = 0
            self.ui.btnRel1.setText("Encender Rele 1")

            self.arduino.write('A') #para el relé 4, los char down son: ASDF
            self.arduinoDice()

if __name__=="__main__":
    app=QtGui.QApplication(sys.argv)
    myapp = Myform()
    myapp.show()
    sys.exit(app.exec_())
