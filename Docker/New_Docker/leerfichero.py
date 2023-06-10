# Leer fichero csv

import csv
import logging

def LecturaFichero(Lectura):
    numeros = []

    try:
        with open(Lectura,newline='') as csvfile:
            csvreader = csv.reader(csvfile, delimiter=',')
            for row in csvreader:
                numeros.append(row)
    except FileNotFoundError:
        print("No existe el fichero numeros.txt")

    return numeros