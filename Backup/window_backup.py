# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'windows_gui.ui'
#
# Created: Thu Dec 29 20:06:46 2016
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
	_fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
	def _fromUtf8(s):
		return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(545, 173)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.Num01 = QtGui.QLineEdit(self.centralwidget)
        self.Num01.setGeometry(QtCore.QRect(10, 110, 31, 27))
        self.Num01.setMaxLength(2)
        self.Num01.setObjectName(_fromUtf8("Num01"))
        self.TitleNum = QtGui.QLabel(self.centralwidget)
        self.TitleNum.setGeometry(QtCore.QRect(10, 80, 71, 17))
        self.TitleNum.setObjectName(_fromUtf8("TitleNum"))
        self.Num02 = QtGui.QLineEdit(self.centralwidget)
        self.Num02.setGeometry(QtCore.QRect(50, 110, 31, 27))
        self.Num02.setMaxLength(2)
        self.Num02.setObjectName(_fromUtf8("Num02"))
        self.Num03 = QtGui.QLineEdit(self.centralwidget)
        self.Num03.setGeometry(QtCore.QRect(90, 110, 31, 27))
        self.Num03.setMaxLength(2)
        self.Num03.setObjectName(_fromUtf8("Num03"))
        self.Num04 = QtGui.QLineEdit(self.centralwidget)
        self.Num04.setGeometry(QtCore.QRect(130, 110, 31, 27))
        self.Num04.setMaxLength(2)
        self.Num04.setObjectName(_fromUtf8("Num04"))
        self.Num05 = QtGui.QLineEdit(self.centralwidget)
        self.Num05.setGeometry(QtCore.QRect(170, 110, 31, 27))
        self.Num05.setMaxLength(2)
        self.Num05.setObjectName(_fromUtf8("Num05"))
        self.TitleStar = QtGui.QLabel(self.centralwidget)
        self.TitleStar.setGeometry(QtCore.QRect(240, 80, 71, 17))
        self.TitleStar.setObjectName(_fromUtf8("TitleStar"))
        self.Star01 = QtGui.QLineEdit(self.centralwidget)
        self.Star01.setGeometry(QtCore.QRect(240, 110, 31, 27))
        self.Star01.setMaxLength(2)
        self.Star01.setObjectName(_fromUtf8("Star01"))
        self.Star02 = QtGui.QLineEdit(self.centralwidget)
        self.Star02.setGeometry(QtCore.QRect(280, 110, 31, 27))
        self.Star02.setMaxLength(2)
        self.Star02.setObjectName(_fromUtf8("Star02"))
        self.Millon = QtGui.QLineEdit(self.centralwidget)
        self.Millon.setGeometry(QtCore.QRect(330, 110, 113, 27))
        self.Millon.setObjectName(_fromUtf8("Millon"))
        self.TitleMillon = QtGui.QLabel(self.centralwidget)
        self.TitleMillon.setGeometry(QtCore.QRect(330, 80, 66, 17))
        self.TitleMillon.setObjectName(_fromUtf8("TitleMillon"))
        self.Diabox = QtGui.QComboBox(self.centralwidget)
        self.Diabox.setGeometry(QtCore.QRect(110, 40, 78, 27))
        self.Diabox.setObjectName(_fromUtf8("Diabox"))
        self.Diabox.addItem(_fromUtf8(""))
        self.Diabox.addItem(_fromUtf8(""))
        self.Diabox.addItem(_fromUtf8(""))
        self.Diabox.addItem(_fromUtf8(""))
        self.Diabox.addItem(_fromUtf8(""))
        self.Diabox.addItem(_fromUtf8(""))
        self.Diabox.addItem(_fromUtf8(""))
        self.Diabox.addItem(_fromUtf8(""))
        self.Diabox.addItem(_fromUtf8(""))
        self.Diabox.addItem(_fromUtf8(""))
        self.Diabox.addItem(_fromUtf8(""))
        self.Diabox.addItem(_fromUtf8(""))
        self.Diabox.addItem(_fromUtf8(""))
        self.Diabox.addItem(_fromUtf8(""))
        self.Diabox.addItem(_fromUtf8(""))
        self.Diabox.addItem(_fromUtf8(""))
        self.Diabox.addItem(_fromUtf8(""))
        self.Diabox.addItem(_fromUtf8(""))
        self.Diabox.addItem(_fromUtf8(""))
        self.Diabox.addItem(_fromUtf8(""))
        self.Diabox.addItem(_fromUtf8(""))
        self.Diabox.addItem(_fromUtf8(""))
        self.Diabox.addItem(_fromUtf8(""))
        self.Diabox.addItem(_fromUtf8(""))
        self.Diabox.addItem(_fromUtf8(""))
        self.Diabox.addItem(_fromUtf8(""))
        self.Diabox.addItem(_fromUtf8(""))
        self.Diabox.addItem(_fromUtf8(""))
        self.Diabox.addItem(_fromUtf8(""))
        self.Diabox.addItem(_fromUtf8(""))
        self.Diabox.addItem(_fromUtf8(""))
        self.Mesbox = QtGui.QComboBox(self.centralwidget)
        self.Mesbox.setGeometry(QtCore.QRect(200, 40, 111, 27))
        self.Mesbox.setObjectName(_fromUtf8("Mesbox"))
        self.Mesbox.addItem(_fromUtf8(""))
        self.Mesbox.addItem(_fromUtf8(""))
        self.Mesbox.addItem(_fromUtf8(""))
        self.Mesbox.addItem(_fromUtf8(""))
        self.Mesbox.addItem(_fromUtf8(""))
        self.Mesbox.addItem(_fromUtf8(""))
        self.Mesbox.addItem(_fromUtf8(""))
        self.Mesbox.addItem(_fromUtf8(""))
        self.Mesbox.addItem(_fromUtf8(""))
        self.Mesbox.addItem(_fromUtf8(""))
        self.Mesbox.addItem(_fromUtf8(""))
        self.Mesbox.addItem(_fromUtf8(""))
        self.Anobox = QtGui.QComboBox(self.centralwidget)
        self.Anobox.setGeometry(QtCore.QRect(320, 40, 78, 27))
        self.Anobox.setObjectName(_fromUtf8("Anobox"))
        self.Anobox.addItem(_fromUtf8(""))
        self.Anobox.addItem(_fromUtf8(""))
        self.Anobox.addItem(_fromUtf8(""))
        self.TitleDia = QtGui.QLabel(self.centralwidget)
        self.TitleDia.setGeometry(QtCore.QRect(110, 10, 66, 17))
        self.TitleDia.setObjectName(_fromUtf8("TitleDia"))
        self.TitleMes = QtGui.QLabel(self.centralwidget)
        self.TitleMes.setGeometry(QtCore.QRect(200, 10, 66, 17))
        self.TitleMes.setObjectName(_fromUtf8("TitleMes"))
        self.TitleAno = QtGui.QLabel(self.centralwidget)
        self.TitleAno.setGeometry(QtCore.QRect(320, 10, 66, 17))
        self.TitleAno.setObjectName(_fromUtf8("TitleAno"))
        self.EraseButton = QtGui.QPushButton(self.centralwidget)
        self.EraseButton.setGeometry(QtCore.QRect(440, 10, 98, 27))
        self.EraseButton.setObjectName(_fromUtf8("EraseButton"))
        self.InsertButton = QtGui.QPushButton(self.centralwidget)
        self.InsertButton.setGeometry(QtCore.QRect(440, 40, 98, 27))
        self.InsertButton.setObjectName(_fromUtf8("InsertButton"))
        self.ExitButton = QtGui.QPushButton(self.centralwidget)
        self.ExitButton.setGeometry(QtCore.QRect(470, 80, 61, 51))
        self.ExitButton.setObjectName(_fromUtf8("ExitButton"))
        self.TitleSem = QtGui.QLabel(self.centralwidget)
        self.TitleSem.setGeometry(QtCore.QRect(10, 10, 66, 17))
        self.TitleSem.setObjectName(_fromUtf8("TitleSem"))
        self.Semanabox = QtGui.QComboBox(self.centralwidget)
        self.Semanabox.setGeometry(QtCore.QRect(10, 40, 91, 27))
        self.Semanabox.setObjectName(_fromUtf8("Semanabox"))
        self.Semanabox.addItem(_fromUtf8(""))
        self.Semanabox.addItem(_fromUtf8(""))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.ExitButton, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.close)
        QtCore.QObject.connect(self.EraseButton, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.EraseMain)
        QtCore.QObject.connect(self.InsertButton, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.InsertMain)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Euromillon 2017", None))
        self.TitleNum.setText(_translate("MainWindow", "Numeros:", None))
        self.TitleStar.setText(_translate("MainWindow", "Estrellas:", None))
        self.Millon.setText(_translate("MainWindow", "NULL", None))
        self.TitleMillon.setText(_translate("MainWindow", "Millón:", None))
        self.Diabox.setItemText(0, _translate("MainWindow", "1", None))
        self.Diabox.setItemText(1, _translate("MainWindow", "2", None))
        self.Diabox.setItemText(2, _translate("MainWindow", "3", None))
        self.Diabox.setItemText(3, _translate("MainWindow", "4", None))
        self.Diabox.setItemText(4, _translate("MainWindow", "5", None))
        self.Diabox.setItemText(5, _translate("MainWindow", "6", None))
        self.Diabox.setItemText(6, _translate("MainWindow", "7", None))
        self.Diabox.setItemText(7, _translate("MainWindow", "8", None))
        self.Diabox.setItemText(8, _translate("MainWindow", "9", None))
        self.Diabox.setItemText(9, _translate("MainWindow", "10", None))
        self.Diabox.setItemText(10, _translate("MainWindow", "11", None))
        self.Diabox.setItemText(11, _translate("MainWindow", "12", None))
        self.Diabox.setItemText(12, _translate("MainWindow", "13", None))
        self.Diabox.setItemText(13, _translate("MainWindow", "14", None))
        self.Diabox.setItemText(14, _translate("MainWindow", "15", None))
        self.Diabox.setItemText(15, _translate("MainWindow", "16", None))
        self.Diabox.setItemText(16, _translate("MainWindow", "17", None))
        self.Diabox.setItemText(17, _translate("MainWindow", "18", None))
        self.Diabox.setItemText(18, _translate("MainWindow", "19", None))
        self.Diabox.setItemText(19, _translate("MainWindow", "20", None))
        self.Diabox.setItemText(20, _translate("MainWindow", "21", None))
        self.Diabox.setItemText(21, _translate("MainWindow", "22", None))
        self.Diabox.setItemText(22, _translate("MainWindow", "23", None))
        self.Diabox.setItemText(23, _translate("MainWindow", "24", None))
        self.Diabox.setItemText(24, _translate("MainWindow", "25", None))
        self.Diabox.setItemText(25, _translate("MainWindow", "26", None))
        self.Diabox.setItemText(26, _translate("MainWindow", "27", None))
        self.Diabox.setItemText(27, _translate("MainWindow", "28", None))
        self.Diabox.setItemText(28, _translate("MainWindow", "29", None))
        self.Diabox.setItemText(29, _translate("MainWindow", "30", None))
        self.Diabox.setItemText(30, _translate("MainWindow", "31", None))
        self.Mesbox.setItemText(0, _translate("MainWindow", "Enero", None))
        self.Mesbox.setItemText(1, _translate("MainWindow", "Febrero", None))
        self.Mesbox.setItemText(2, _translate("MainWindow", "Marzo", None))
        self.Mesbox.setItemText(3, _translate("MainWindow", "Abril", None))
        self.Mesbox.setItemText(4, _translate("MainWindow", "Mayo", None))
        self.Mesbox.setItemText(5, _translate("MainWindow", "Junio", None))
        self.Mesbox.setItemText(6, _translate("MainWindow", "Julio", None))
        self.Mesbox.setItemText(7, _translate("MainWindow", "Agosto", None))
        self.Mesbox.setItemText(8, _translate("MainWindow", "Septiembre", None))
        self.Mesbox.setItemText(9, _translate("MainWindow", "Octubre", None))
        self.Mesbox.setItemText(10, _translate("MainWindow", "Noviembre", None))
        self.Mesbox.setItemText(11, _translate("MainWindow", "Diciembre", None))
        self.Anobox.setItemText(0, _translate("MainWindow", "2016", None))
        self.Anobox.setItemText(1, _translate("MainWindow", "2017", None))
        self.Anobox.setItemText(2, _translate("MainWindow", "2018", None))
        self.TitleDia.setText(_translate("MainWindow", "Dia:", None))
        self.TitleMes.setText(_translate("MainWindow", "Mes:", None))
        self.TitleAno.setText(_translate("MainWindow", "Año:", None))
        self.EraseButton.setText(_translate("MainWindow", "Borrar", None))
        self.InsertButton.setText(_translate("MainWindow", "Insertar", None))
        self.ExitButton.setText(_translate("MainWindow", "EXIT", None))
        self.TitleSem.setText(_translate("MainWindow", "Semana:", None))
        self.Semanabox.setItemText(0, _translate("MainWindow", "Martes", None))
        self.Semanabox.setItemText(1, _translate("MainWindow", "Viernes", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

