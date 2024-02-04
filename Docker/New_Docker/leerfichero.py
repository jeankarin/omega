# Leer fichero csv

import csv
import logging

def LecturaFichero(Lectura):
    numeros = []

    LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
    logging.basicConfig(filename = "/opt/files/message.log",
        level = logging.DEBUG,
        format = LOG_FORMAT)
    logger = logging.getLogger()

    try:
        with open(Lectura,newline='') as csvfile:
            csvreader = csv.reader(csvfile, delimiter=',')
            for row in csvreader:
                numeros.append(row)
    except FileNotFoundError:
        logger.error("Lectura fichero: No existe o error leyendo el fichero numeros.txt ó lastregistry.txt")
        csvfile.close()
        return 1

    csvfile.close()
    return numeros