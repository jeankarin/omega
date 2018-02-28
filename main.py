#!/usr/bin/python

import sys, os, time

from PyQt4.QtGui import *
from window import *


class MainWindow(QtGui.QMainWindow):
	def __init__(self,parent=None):
		super(MainWindow, self).__init__(parent)
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		

	def EraseMain(self):
		print("HOLA")
		
	def InsertMain(self):
		print("HOLA")

if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	myapp = MainWindow()
	myapp.show()
	sys.exit(app.exec_())
