# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ristorante_5.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(262, 64)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.button_cancella = QtWidgets.QPushButton(self.centralwidget)
        self.button_cancella.setObjectName("button_cancella")
        self.gridLayout.addWidget(self.button_cancella, 2, 1, 1, 1)
        self.button_annulla = QtWidgets.QPushButton(self.centralwidget)
        self.button_annulla.setObjectName("button_annulla")
        self.gridLayout.addWidget(self.button_annulla, 2, 2, 1, 1)
        self.button_apri = QtWidgets.QPushButton(self.centralwidget)
        self.button_apri.setObjectName("button_apri")
        self.gridLayout.addWidget(self.button_apri, 2, 0, 1, 1)
        self.testo = QtWidgets.QLabel(self.centralwidget)
        self.testo.setAlignment(QtCore.Qt.AlignCenter)
        self.testo.setObjectName("testo")
        self.gridLayout.addWidget(self.testo, 1, 0, 1, 3)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.button_cancella.setText(_translate("MainWindow", "Cancella"))
        self.button_annulla.setText(_translate("MainWindow", "Annulla"))
        self.button_apri.setText(_translate("MainWindow", "Apri"))
        self.testo.setText(_translate("MainWindow", "Il tavolo è prenotato da , cosa vuoi fare?"))
