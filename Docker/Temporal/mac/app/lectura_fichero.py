"""
Aquí leemos el fichero numeros.txt que hemos creado con los sorteos pendientes de añadir y
comprobamos también que tenga la información correcta
"""

import csv
import logging

def lecturaFichero(lectura):
    numeros = []

    LOG_FORMAT = "%(levelname)s %(asctime)s = %(message)s"
    logging.basicConfig(filename = "~/DevLocal/git/omega/Docker/Temporal/mac/files/message.log",
                        level = logging.DEBUG,
                        format = LOG_FORMAT)
    logger = logging.getLogger()

    try:
        with open(lectura, newline = '') as csvfile:
            csvreader = csv.reader(csvfile, delimiter = ',')
            for row in csvreader:
                numeros.append(row)
    except FileNotFoundError:
            logger.error("Lectura fichero: No existe el fichero numeros.txt ó error leyendo el fichero")
            return 1

    return numeros

# Comprobamos que el fichero tenga la información correcta
def checkErrorFile(numeros):
    error = 0

    LOG_FORMAT = "%(levelname)s %(asctime)s = %(message)s"
    logging.basicConfig(filename = "~/DevLocal/git/omega/Docker/Temporal/mac/files/message.log",
                        level = logging.DEBUG,
                        format = LOG_FORMAT)
    logger = logging.getLogger()

    meses = ["'Enero'","'Febrero'","'Marzo'","'Abril'","'Mayo'","'Junio'","'Julio'","'Agosto'","'Septiembre'","'Octubre'","'Noviembre'","'Diciembre'"]
    dias = ["'Martes'","'Viernes'"]

    try:
        for i in range(len(numeros)):
            if (numeros[i][7] not in dias):
                logger.error("Error en numeros.txt Día mal indicado.")
                error += 1
            if (numeros[i][9] not in meses):
                    logger.error("Error en numeros.txt Mes mal indicado.")
                    error += 1
            if type(numeros[i][11]) == False:
                    logger.error("Error en numeros.txt Millon mal indicado.")
                    error += 1
    except IndexError:
         logger.error("El fichero numeros.txt está mal creado")
         error += 1
    
    return error