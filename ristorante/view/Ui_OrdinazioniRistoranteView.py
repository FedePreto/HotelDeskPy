'''
__author__: Alessandro Rongoni, Gregorio Vecchiola
'''
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QCursor


class Ui_OrdinazioniRistoranteView(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow_ordinazione")
        MainWindow.resize(1397, 632)
        MainWindow.setMinimumSize(QtCore.QSize(1397, 632))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ui/resources/logo/logo_small_icon_only_inverted.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setStyleSheet("#MainWindow_ordinazione{background-image: url(ui/resources/ristorante/50-504378_restaurant-hd-wallpaper-restaurant-hd.jpg);}")
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 255, 140), stop:1 rgba(255, 255, 255, 165));")
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.lineE_tavolo = QtWidgets.QLineEdit(self.centralwidget)
        self.lineE_tavolo.setEnabled(True)
        self.lineE_tavolo.setMinimumSize(QtCore.QSize(70, 0))
        self.lineE_tavolo.setMaximumSize(QtCore.QSize(70, 16777215))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineE_tavolo.setFont(font)
        self.lineE_tavolo.setAlignment(QtCore.Qt.AlignCenter)
        self.lineE_tavolo.setReadOnly(True)
        self.lineE_tavolo.setObjectName("LE_tavolo")
        self.horizontalLayout_2.addWidget(self.lineE_tavolo)
        self.horizontalLayout_6.addLayout(self.horizontalLayout_2)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 255, 140), stop:1 rgba(255, 255, 255, 165));")
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_3.addWidget(self.label_13)
        self.lineE_nominativo = QtWidgets.QLineEdit(self.centralwidget)
        self.lineE_nominativo.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineE_nominativo.sizePolicy().hasHeightForWidth())
        self.lineE_nominativo.setSizePolicy(sizePolicy)
        self.lineE_nominativo.setMinimumSize(QtCore.QSize(400, 0))
        self.lineE_nominativo.setMaximumSize(QtCore.QSize(600, 16777215))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineE_nominativo.setFont(font)
        self.lineE_nominativo.setReadOnly(True)
        self.lineE_nominativo.setObjectName("LE_nominativo")
        self.horizontalLayout_3.addWidget(self.lineE_nominativo)
        self.horizontalLayout_6.addLayout(self.horizontalLayout_3)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 255, 140), stop:1 rgba(255, 255, 255, 165));")
        self.label_10.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_4.addWidget(self.label_10)
        self.lineE_persone = QtWidgets.QLineEdit(self.centralwidget)
        self.lineE_persone.setEnabled(True)
        self.lineE_persone.setMinimumSize(QtCore.QSize(75, 0))
        self.lineE_persone.setMaximumSize(QtCore.QSize(75, 16777215))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineE_persone.setFont(font)
        self.lineE_persone.setReadOnly(True)
        self.lineE_persone.setObjectName("LE_persone")
        self.horizontalLayout_4.addWidget(self.lineE_persone)
        self.horizontalLayout_6.addLayout(self.horizontalLayout_4)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem2)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 255, 140), stop:1 rgba(255, 255, 255, 165));")
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_5.addWidget(self.label_11)
        self.cB_pagamento = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cB_pagamento.sizePolicy().hasHeightForWidth())
        self.cB_pagamento.setSizePolicy(sizePolicy)
        self.cB_pagamento.setMinimumSize(QtCore.QSize(150, 0))
        self.cB_pagamento.setMaximumSize(QtCore.QSize(150, 16777215))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.cB_pagamento.setFont(font)
        self.cB_pagamento.setObjectName("cB_pagamento")
        self.cB_pagamento.addItem("")
        self.cB_pagamento.addItem("")
        self.cB_pagamento.addItem("")
        self.set_combo(self.cB_pagamento, font)
        self.horizontalLayout_5.addWidget(self.cB_pagamento)
        self.horizontalLayout_6.addLayout(self.horizontalLayout_5)
        self.gridLayout_2.addLayout(self.horizontalLayout_6, 0, 0, 1, 2)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_2.addWidget(self.line, 2, 0, 1, 2)
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout_2.addWidget(self.line_3, 3, 0, 1, 2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem3 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem3)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 255, 140), stop:1 rgba(255, 255, 255, 165));")
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_9.addWidget(self.label_12)
        spacerItem4 = QtWidgets.QSpacerItem(70, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem4)
        self.lineE_coperto = QtWidgets.QLineEdit(self.centralwidget)
        self.lineE_coperto.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineE_coperto.sizePolicy().hasHeightForWidth())
        self.lineE_coperto.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineE_coperto.setFont(font)
        self.lineE_coperto.setAlignment(QtCore.Qt.AlignCenter)
        self.lineE_coperto.setObjectName("LE_coperto")
        self.horizontalLayout_9.addWidget(self.lineE_coperto)
        self.verticalLayout.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 255, 140), stop:1 rgba(255, 255, 255, 165));")
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_10.addWidget(self.label_14)
        spacerItem5 = QtWidgets.QSpacerItem(78, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem5)
        self.lineE_sconto = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineE_sconto.sizePolicy().hasHeightForWidth())
        self.lineE_sconto.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineE_sconto.setFont(font)
        self.lineE_sconto.setAlignment(QtCore.Qt.AlignCenter)
        self.lineE_sconto.setObjectName("LE_sconto")
        self.horizontalLayout_10.addWidget(self.lineE_sconto)
        self.verticalLayout.addLayout(self.horizontalLayout_10)
        self.gridLayout_2.addLayout(self.verticalLayout, 4, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 255, 140), stop:1 rgba(255, 255, 255, 165));")
        self.label_16.setObjectName("label_16")
        self.gridLayout.addWidget(self.label_16, 2, 0, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 255, 140), stop:1 rgba(255, 255, 255, 165));")
        self.label_15.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_15.setObjectName("label_15")
        self.gridLayout.addWidget(self.label_15, 1, 0, 1, 1)
        self.lineE_totale = QtWidgets.QLineEdit(self.centralwidget)
        self.lineE_totale.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineE_totale.sizePolicy().hasHeightForWidth())
        self.lineE_totale.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lineE_totale.setFont(font)
        self.lineE_totale.setAlignment(QtCore.Qt.AlignCenter)
        self.lineE_totale.setReadOnly(True)
        self.lineE_totale.setObjectName("LE_totale")
        self.gridLayout.addWidget(self.lineE_totale, 1, 1, 1, 1)
        self.lineE_totale_per_persona = QtWidgets.QLineEdit(self.centralwidget)
        self.lineE_totale_per_persona.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineE_totale_per_persona.sizePolicy().hasHeightForWidth())
        self.lineE_totale_per_persona.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lineE_totale_per_persona.setFont(font)
        self.lineE_totale_per_persona.setAlignment(QtCore.Qt.AlignCenter)
        self.lineE_totale_per_persona.setReadOnly(True)
        self.lineE_totale_per_persona.setObjectName("LE_totale_per_persona")
        self.gridLayout.addWidget(self.lineE_totale_per_persona, 2, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 4, 1, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout_2.addWidget(self.line_2, 5, 0, 1, 2)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.cB_dolci = QtWidgets.QComboBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.cB_dolci.setFont(font)
        self.cB_dolci.setObjectName("cB_dolci")
        self.cB_dolci.addItem("")
        self.set_combo(self.cB_dolci, font)
        self.gridLayout_3.addWidget(self.cB_dolci, 10, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 255, 140), stop:1 rgba(255, 255, 255, 165));")
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 5, 0, 1, 1)
        self.cB_frutta = QtWidgets.QComboBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.cB_frutta.setFont(font)
        self.cB_frutta.setObjectName("cB_frutta")
        self.cB_frutta.addItem("")
        self.set_combo(self.cB_frutta, font)
        self.gridLayout_3.addWidget(self.cB_frutta, 11, 1, 1, 1)
        self.cB_bevande = QtWidgets.QComboBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.cB_bevande.setFont(font)
        self.cB_bevande.setObjectName("cB_bevande")
        self.cB_bevande.addItem("")
        self.set_combo(self.cB_bevande, font)
        self.gridLayout_3.addWidget(self.cB_bevande, 12, 1, 1, 1)
        self.cB_antipasti = QtWidgets.QComboBox(self.centralwidget)
        self.cB_antipasti.setMinimumSize(QtCore.QSize(400, 0))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.cB_antipasti.setFont(font)
        self.cB_antipasti.setObjectName("cB_antipasti")
        self.cB_antipasti.addItem("")
        self.set_combo(self.cB_antipasti, font)
        self.gridLayout_3.addWidget(self.cB_antipasti, 3, 1, 1, 1)
        self.pB_bevande = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pB_bevande.setFont(font)
        self.pB_bevande.setObjectName("pB_bevande")
        self.pB_bevande.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.gridLayout_3.addWidget(self.pB_bevande, 12, 2, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 255, 140), stop:1 rgba(255, 255, 255, 165));")
        self.label_7.setObjectName("label_7")
        self.gridLayout_3.addWidget(self.label_7, 11, 0, 1, 1)
        self.pB_antipasti = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pB_antipasti.setFont(font)
        self.pB_antipasti.setObjectName("pB_antipasti")
        self.pB_antipasti.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.gridLayout_3.addWidget(self.pB_antipasti, 3, 2, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 255, 140), stop:1 rgba(255, 255, 255, 165));")
        self.label_8.setObjectName("label_8")
        self.gridLayout_3.addWidget(self.label_8, 12, 0, 1, 1)
        self.pB_frutta = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pB_frutta.setFont(font)
        self.pB_frutta.setObjectName("pB_frutta")
        self.pB_frutta.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.gridLayout_3.addWidget(self.pB_frutta, 11, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 255, 140), stop:1 rgba(255, 255, 255, 165));")
        self.label_4.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.label_4, 7, 0, 1, 1)
        self.pB_contorni = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pB_contorni.setFont(font)
        self.pB_contorni.setObjectName("pB_contorni")
        self.pB_contorni.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.gridLayout_3.addWidget(self.pB_contorni, 9, 2, 1, 1)
        self.pB_secondi = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pB_secondi.setFont(font)
        self.pB_secondi.setObjectName("pB_secondi")
        self.pB_secondi.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.gridLayout_3.addWidget(self.pB_secondi, 7, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 255, 140), stop:1 rgba(255, 255, 255, 165));")
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.label_5, 10, 0, 1, 1)
        self.cB_contorni = QtWidgets.QComboBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.cB_contorni.setFont(font)
        self.cB_contorni.setObjectName("cB_contorni")
        self.cB_contorni.addItem("")
        self.set_combo(self.cB_contorni, font)
        self.gridLayout_3.addWidget(self.cB_contorni, 9, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 255, 140), stop:1 rgba(255, 255, 255, 165));")
        self.label_6.setObjectName("label_6")
        self.gridLayout_3.addWidget(self.label_6, 9, 0, 1, 1)
        self.cB_secondi = QtWidgets.QComboBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.cB_secondi.setFont(font)
        self.cB_secondi.setObjectName("cB_secondi")
        self.cB_secondi.addItem("")
        self.set_combo(self.cB_secondi, font)
        self.gridLayout_3.addWidget(self.cB_secondi, 7, 1, 1, 1)
        self.cB_primi = QtWidgets.QComboBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.cB_primi.setFont(font)
        self.cB_primi.setObjectName("cB_primi")
        self.cB_primi.addItem("")
        self.set_combo(self.cB_primi, font)
        self.gridLayout_3.addWidget(self.cB_primi, 5, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 255, 140), stop:1 rgba(255, 255, 255, 165));")
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 3, 0, 1, 1)
        self.pB_dolci = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pB_dolci.setFont(font)
        self.pB_dolci.setObjectName("pB_dolci")
        self.pB_dolci.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.gridLayout_3.addWidget(self.pB_dolci, 10, 2, 1, 1)
        self.pB_primi = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pB_primi.setFont(font)
        self.pB_primi.setObjectName("pB_primi")
        self.pB_primi.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.gridLayout_3.addWidget(self.pB_primi, 5, 2, 1, 1)
        self.horizontalLayout_7.addLayout(self.gridLayout_3)
        self.tW_scontrino_tavolo = QtWidgets.QTableWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.tW_scontrino_tavolo.setFont(font)
        self.tW_scontrino_tavolo.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(255, 255, 255, 225), stop:1 rgba(255, 255, 255, 227));")
        self.tW_scontrino_tavolo.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tW_scontrino_tavolo.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.tW_scontrino_tavolo.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tW_scontrino_tavolo.setObjectName("tW_scontrino_tavolo")
        self.tW_scontrino_tavolo.setColumnCount(4)
        self.tW_scontrino_tavolo.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tW_scontrino_tavolo.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tW_scontrino_tavolo.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tW_scontrino_tavolo.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tW_scontrino_tavolo.setHorizontalHeaderItem(3, item)
        self.tW_scontrino_tavolo.horizontalHeader().setDefaultSectionSize(280)
        self.tW_scontrino_tavolo.horizontalHeader().setStretchLastSection(True)
        self.horizontalLayout_7.addWidget(self.tW_scontrino_tavolo)
        self.gridLayout_2.addLayout(self.horizontalLayout_7, 1, 0, 1, 2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pB_conferma = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pB_conferma.setFont(font)
        self.pB_conferma.setObjectName("pB_conferma")
        self.pB_conferma.setEnabled(False)
        self.pB_conferma.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.horizontalLayout.addWidget(self.pB_conferma)
        self.pB_cancella = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pB_cancella.setFont(font)
        self.pB_cancella.setObjectName("pB_cancella")
        self.pB_cancella.setEnabled(False)
        self.pB_cancella.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.horizontalLayout.addWidget(self.pB_cancella)
        self.pB_annulla = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pB_annulla.setFont(font)
        self.pB_annulla.setIconSize(QtCore.QSize(16, 16))
        self.pB_annulla.setObjectName("pB_chiudi_tavolo")
        self.pB_annulla.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.horizontalLayout.addWidget(self.pB_annulla)
        self.gridLayout_2.addLayout(self.horizontalLayout, 6, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.pB_Aggiungi = [self.pB_antipasti, self.pB_primi,self.pB_secondi, self.pB_contorni, self.pB_bevande, self.pB_frutta, self.pB_dolci]

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def set_combo(self, combo, font):
        combo.setEditable(True)
        line_e = combo.lineEdit()
        line_e.setAlignment(QtCore.Qt.AlignCenter)
        line_e.setFont(font)
        line_e.setReadOnly(True)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Chiusura Conto Tavolo"))
        self.label.setText(_translate("MainWindow", "Tavolo: "))
        self.label_13.setText(_translate("MainWindow", "Nominativo:"))
        self.label_10.setText(_translate("MainWindow", "Persone:"))
        self.label_11.setText(_translate("MainWindow", "Metodo di pagamento:"))
        self.cB_pagamento.setItemText(0, _translate("MainWindow", ""))
        self.cB_pagamento.setItemText(1, _translate("MainWindow", "Contanti"))
        self.cB_pagamento.setItemText(2, _translate("MainWindow", "Carta"))
        self.label_12.setText(_translate("MainWindow", "Coperto (€):"))
        self.lineE_coperto.setText(_translate("MainWindow", "1.50"))
        self.label_14.setText(_translate("MainWindow", "Sconto (%):"))
        self.lineE_sconto.setText(_translate("MainWindow", "0"))
        self.label_16.setText(_translate("MainWindow", "Totale per persona:"))
        self.label_15.setText(_translate("MainWindow", "Totale:"))
        self.lineE_totale.setText(_translate("MainWindow", "0,00 €"))
        self.lineE_totale_per_persona.setText(_translate("MainWindow", "0,00 €"))
        self.label_3.setText(_translate("MainWindow", "Primi:"))
        self.pB_bevande.setText(_translate("MainWindow", "Aggiungi"))
        self.label_7.setText(_translate("MainWindow", "Frutta:"))
        self.pB_antipasti.setText(_translate("MainWindow", "Aggiungi"))
        self.label_8.setText(_translate("MainWindow", "Bevande:"))
        self.pB_frutta.setText(_translate("MainWindow", "Aggiungi"))
        self.label_4.setText(_translate("MainWindow", "Secondi:"))
        self.pB_contorni.setText(_translate("MainWindow", "Aggiungi"))
        self.pB_secondi.setText(_translate("MainWindow", "Aggiungi"))
        self.label_5.setText(_translate("MainWindow", "Dolci:"))
        self.label_6.setText(_translate("MainWindow", "Contorni:"))
        self.label_2.setText(_translate("MainWindow", "Antipasti:"))
        self.pB_dolci.setText(_translate("MainWindow", "Aggiungi"))
        self.pB_primi.setText(_translate("MainWindow", "Aggiungi"))
        item = self.tW_scontrino_tavolo.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Ordine"))
        item = self.tW_scontrino_tavolo.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Quantità"))
        item = self.tW_scontrino_tavolo.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Prezzo Unitario"))
        item = self.tW_scontrino_tavolo.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Totale"))
        self.pB_conferma.setText(_translate("MainWindow", "Conferma"))
        self.pB_cancella.setText(_translate("MainWindow", "Cancella ordine"))
        self.pB_annulla.setText(_translate("MainWindow", "Annulla"))
