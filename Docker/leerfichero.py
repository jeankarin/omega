# Leer fichero csv

import csv

def LecturaFichero(Lectura):
    numeros = []
    with open(Lectura,newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        for row in csvreader:
            numeros.append(row)
    
    return numeros