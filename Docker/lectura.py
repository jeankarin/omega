import csv

def LecturaFichero(Lectura):
	numeros = []
	fichero = open(Lectura,'r')
	lineas = csv.reader(fichero)
	for line in lineas:
		numeros.append(line)

	return numeros