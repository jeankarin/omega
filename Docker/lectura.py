import csv


def LecturaFichero(Lectura):
    numeros = []
    fichero = open(Lectura, 'r')
    lineas = csv.reader(fichero)
    for line in lineas:
        numeros.append(line)

    return numeros

def confMillones(fichero):
    a = 0
    for i in fichero:
        if (i.isdigit() == True):
            a = a + 1
    return a
