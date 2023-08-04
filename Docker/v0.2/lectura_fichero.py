"""
Aquí leemos el fichero numeros.txt que hemos creado con los sorteos pendientes de añadir y
comprobamos también que tenga la información correcta
"""

import csv
import logging_class

def lecturaFichero(lectura):
    numeros = []

    logError1 = logging_class.checkError()

    try:
        with open(lectura, newline = '') as csvfile:
            csvreader = csv.reader(csvfile, delimiter = ',')
            for row in csvreader:
                numeros.append(row)
    except FileNotFoundError:
            logError1.lecturaFichero()
            return 1

    return numeros

# Comprobamos que el fichero tenga la información correcta
def checkErrorFile(numeros):
    error = 0
    logError2 = logging_class.checkError()

    meses = ["'Enero'","'Febrero'","'Marzo'","'Abril'","'Mayo'","'Junio'","'Julio'","'Agosto'","'Septiembre'","'Octubre'","'Noviembre'","'Diciembre'"]
    dias = ["'Martes'","'Viernes'"]

    try:
        for i in range(len(numeros)):
            if (numeros[i][7] not in dias):
                logError2.errorNum(1)
                error += 1
            if (numeros[i][9] not in meses):
                    logError2.errorNum(2)
                    error += 1
            if type(numeros[i][11]) == False:
                    logError2.errorNum(3)
                    error += 1
    except IndexError:
         logError2.errorNum(4)
         error += 1
    
    return error