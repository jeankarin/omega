#!/usr/bin/python

import sys, os, time

from PyQt4.QtGui import *
from window import *
from insert import Insert_to_database

class MainWindow(QtGui.QMainWindow):
	def __init__(self,parent=None):
		super(MainWindow, self).__init__(parent)
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)

	def EraseMain(self):
		self.ui.Num01.setText("")
		self.ui.Num02.setText("")
		self.ui.Num03.setText("")
		self.ui.Num04.setText("")
		self.ui.Num05.setText("")
		self.ui.Star01.setText("")
		self.ui.Star02.setText("")
		self.ui.Millon.setText("NULL")
		
	def InsertMain(self):
		#Creamos variable que cogera los datos
		num=[]
		num.append(int(self.ui.Num01.text()))
		num.append(int(self.ui.Num02.text()))
		num.append(int(self.ui.Num03.text()))
		num.append(int(self.ui.Num04.text()))
		num.append(int(self.ui.Num05.text()))
		num.append(int(self.ui.Star01.text()))
		num.append(int(self.ui.Star02.text()))
		num.append('\'' + str(self.ui.Semanabox.currentText() + '\''))
		num.append(int(self.ui.Diabox.currentText()))
		num.append('\'' + str(self.ui.Mesbox.currentText() + '\''))
		num.append(int(self.ui.Anobox.currentText()))
		#num.append('\'' + str(self.ui.Millon.text() + '\''))
		num.append(self.ui.Millon.text())
		Insert_to_database(num)

if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	myapp = MainWindow()
	myapp.show()
	sys.exit(app.exec_())
