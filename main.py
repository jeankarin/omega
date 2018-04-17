#-*-coding:latin-1-*-
"""
Author: JeanKarin
14/04/2018 21:02
Euromillon v0.0.1
"""

def consulta(opcion,num):
	#Agafem la consulta que volem fer servir.
	if opcion <= 1:
		consulta = queries.ConsultaFinal()
		return consulta
	else:
		consulta = queries.InsertOne(num)
		return consulta


def MySQL1(sqlsent):
	#Crearem el cursor i li pasem la consulta.
	datos = []
	datos = connection.Consulta_db(sqlsent)

	#Mostrem el resultat per pantalla
	visualcons.VisualCons(datos)

def main():
	os.system('clear')
	num = []
	while True:
		print ("1. Consulta")
		print ("2. Insert")
		print ("3. Salir")
		option = input ("Opcio: ")
		if option > 2:
			break
		elif option == 1:
			sql = consulta(1,num)
			MySQL1(sql)
		else:
			sql = consulta(2,num)
			print (sql)


if __name__ == '__main__':
	import queries, connection, os, visualcons, numbers
	main()