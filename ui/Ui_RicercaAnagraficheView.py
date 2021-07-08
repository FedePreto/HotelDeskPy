# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ricerca_anagrafiche.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(615, 165)
        MainWindow.setMinimumSize(QtCore.QSize(615, 165))
        MainWindow.setMaximumSize(QtCore.QSize(615, 165))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("resources/logo/logo_small.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("")
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.cB_criterio_ricerca = QtWidgets.QComboBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.cB_criterio_ricerca.setFont(font)
        self.cB_criterio_ricerca.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.cB_criterio_ricerca.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.cB_criterio_ricerca.setObjectName("cB_criterio_ricerca")
        self.cB_criterio_ricerca.addItem("")
        self.cB_criterio_ricerca.addItem("")
        self.cB_criterio_ricerca.addItem("")
        self.cB_criterio_ricerca.addItem("")
        self.cB_criterio_ricerca.addItem("")
        self.gridLayout_2.addWidget(self.cB_criterio_ricerca, 0, 1, 1, 1)
        self.lineE_parola = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineE_parola.setFont(font)
        self.lineE_parola.setAlignment(QtCore.Qt.AlignCenter)
        self.lineE_parola.setClearButtonEnabled(True)
        self.lineE_parola.setObjectName("lineE_parola")
        self.gridLayout_2.addWidget(self.lineE_parola, 1, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("")
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pB_ricerca = QtWidgets.QPushButton(self.centralwidget)
        self.pB_ricerca.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pB_ricerca.sizePolicy().hasHeightForWidth())
        self.pB_ricerca.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pB_ricerca.setFont(font)
        self.pB_ricerca.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pB_ricerca.setObjectName("pB_ricerca")
        self.horizontalLayout.addWidget(self.pB_ricerca)
        self.pB_annulla = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pB_annulla.setFont(font)
        self.pB_annulla.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pB_annulla.setObjectName("pB_annulla")
        self.horizontalLayout.addWidget(self.pB_annulla)
        self.verticalLayout.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Ricerca Anagrafiche"))
        self.label.setText(_translate("MainWindow", "Seleziona il criterio di ricerca:"))
        self.cB_criterio_ricerca.setItemText(0, _translate("MainWindow", "ID"))
        self.cB_criterio_ricerca.setItemText(1, _translate("MainWindow", "NOME"))
        self.cB_criterio_ricerca.setItemText(2, _translate("MainWindow", "COGNOME"))
        self.cB_criterio_ricerca.setItemText(3, _translate("MainWindow", "SESSO"))
        self.cB_criterio_ricerca.setItemText(4, _translate("MainWindow", "DATA_NASCITA"))
        self.label_2.setText(_translate("MainWindow", "Inserisci la parola chiave:"))
        self.pB_ricerca.setText(_translate("MainWindow", "Ricerca"))
        self.pB_annulla.setText(_translate("MainWindow", "Annulla"))
