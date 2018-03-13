#-*-coding:latin-1-*-
"""
MySQL connection
"""
import MySQLdb
import queries

class Connect(object):
	def __init__(self):
		#Datos de conexión
		self.db = MySQLdb.connect(host="localhost",user="euromillon_test",passwd="Inicio18",db="EUROMILLON_TEST")

	def cursor(self):
		#Creamos un objeto Cursor. Que permitirá
		#ejecutar todas las queries que necesitas
		self.cur = self.db.cursor()

	def close(self):
		self.cur.close()

	def executer(self,sql_statement):
		self.cur.execute(sql_statement)
		return self.cur.fetchall()

def Consulta_db():
	con = Connect()
	con.cursor()

	consulta = queries.ConsultaFinal()

	resultado = con.executer(consulta)

	con.close

	return resultado