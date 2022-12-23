# Leer fichero csv

import csv

def LecturaFichero(Lectura):
    numeros = []
    with open(Lectura,newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in spamreader:
            numeros.append(row)
    
    return numeros