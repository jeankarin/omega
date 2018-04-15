#-*-coding:latin-1-*-
"""
Author: JeanKarin
14/04/2018 21:02
Euromillon v0.0.1
"""

def consulta():
	os.system('clear')
	#Agafem la consulta que volem fer servir.
	consulta = queries.ConsultaFinal()
	return consulta


def MySQL1(sqlsent):
	#Crearem el cursor i li pasem la consulta.
	datos = []
	datos = connection.Consulta_db(sqlsent)

	#Mostrem el resultat per pantalla
	print (datos)

def main():
	os.system('clear')
	while True:
		print ("1. Consulta")
		print ("2. Insert")
		print ("3. Salir")
		option = input ("Opcio: ")
		if option > 2:
			break
		elif option == 1:
			sql = consulta()
			MySQL1(sql)
		else:
			os.system('clear')
			print ("Gracies per escullir-me")


if __name__ == '__main__':
	import queries, connection, os
	main()