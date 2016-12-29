#!/usr/bin/python
#-*-coding:latin-1-*-
import MySQLdb

class Connect(object):
	def __init__(self):
		self.db = MySQLdb.Connect("localhost","euromillon_user","Inicio15","EUROMILLON_DB_PRE")

	def cursor(self):
		self.cursor = self.db.cursor()
		return self.cursor

	def close(self):
		self.cursor.close()

	def executer(self,sql_statement):
		self.cursor.execute(sql_statement)
		return self.cursor.fetchall()

	def executerins(self,sql_statement):
		try:
			self.cursor.execute(sql_statement)
			self.db.commit()
		except:
			self.db.rollback()
