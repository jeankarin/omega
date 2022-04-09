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
    b = 0
    for i in range(len(fichero)):
        b = fichero[0][0]
        if (fichero[i][0].isdigit()):
            a = a + 1
    return a
