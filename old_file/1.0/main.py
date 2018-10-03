#!/usr/bin/python

# Lectura fichero csv
def LecturaFichero():
	numeros = []
	fichero = open('numeros.txt','r')
	lineas = csv.reader(fichero)
	for line in lineas:
		numeros.append(line)

	return numeros

# Funcion principal
def main():
	euro = LecturaFichero()
	consulta = SqlStatement(euro)

	InsertData(consulta)

if __name__ == '__main__':
	import csv
	from sql_insert import SqlStatement
	from mysql_con import *
	main()