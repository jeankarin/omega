# Leer fichero csv

import csv

def LecturaFichero(Lectura):
    numeros = []
    with open(Lectura,newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in csvreader:
            numeros.append(row)
    
    return numeros