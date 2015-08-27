# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventanaControlArduino.ui'
#
# Created: Sun Aug 11 21:41:10 2013
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(282, 386)
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Control Arduino", None, QtGui.QApplication.UnicodeUTF8))
        self.txtArduino = QtGui.QTextBrowser(Form)
        self.txtArduino.setGeometry(QtCore.QRect(10, 10, 256, 192))
        self.txtArduino.setObjectName(_fromUtf8("txtArduino"))
        self.btnRel4 = QtGui.QPushButton(Form)
        self.btnRel4.setGeometry(QtCore.QRect(70, 220, 131, 27))
        self.btnRel4.setText(QtGui.QApplication.translate("Form", "Encender Relé 4", None, QtGui.QApplication.UnicodeUTF8))
        self.btnRel4.setObjectName(_fromUtf8("btnRel4"))
        self.btnRel3 = QtGui.QPushButton(Form)
        self.btnRel3.setGeometry(QtCore.QRect(70, 260, 131, 27))
        self.btnRel3.setText(QtGui.QApplication.translate("Form", "Encender Relé 3", None, QtGui.QApplication.UnicodeUTF8))
        self.btnRel3.setObjectName(_fromUtf8("btnRel3"))
        self.btnRel2 = QtGui.QPushButton(Form)
        self.btnRel2.setGeometry(QtCore.QRect(70, 300, 131, 27))
        self.btnRel2.setText(QtGui.QApplication.translate("Form", "Encender Relé 2", None, QtGui.QApplication.UnicodeUTF8))
        self.btnRel2.setObjectName(_fromUtf8("btnRel2"))
        self.btnRel1 = QtGui.QPushButton(Form)
        self.btnRel1.setGeometry(QtCore.QRect(70, 340, 131, 27))
        self.btnRel1.setText(QtGui.QApplication.translate("Form", "Encender Relé 1", None, QtGui.QApplication.UnicodeUTF8))
        self.btnRel1.setObjectName(_fromUtf8("btnRel1"))

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.btnRel4, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.rele4)
        QtCore.QObject.connect(self.btnRel3, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.rele3)
        QtCore.QObject.connect(self.btnRel2, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.rele2)
        QtCore.QObject.connect(self.btnRel1, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.rele1)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        pass

