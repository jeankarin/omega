#!/usr/bin/python

# Lectura fichero csv
def LecturaFichero(Lectura):
	numeros = []
	fichero = open(Lectura,'r')
	lineas = csv.reader(fichero)
	for line in lineas:
		numeros.append(line)

	return numeros

# Funcion principal
def main():
	option = True

	while option:
		print ("1. Numeros\n2. Millones\n3. Salir")
		option = input("Seleccione una opcion:")
		if (option == 1):
			euro = LecturaFichero('numeros.txt')
			consulta = SqlStatement(euro)
			if (consulta != 0):
				InsertData(consulta)
		elif (option == 2):
			euro = LecturaFichero('millones.txt')
			consmill = SqlStatement2(euro)
			InsertData(consmill)
		elif (option == 3):
			option = False

if __name__ == '__main__':
	import csv
	from sql_insert import SqlStatement
	from sql_insert import SqlStatement2
	from mysql_con import *
	main()