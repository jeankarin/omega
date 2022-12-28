# Leer fichero csv

import csv
import logging

def LecturaFichero(Lectura):
    numeros = []

    LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
    logging.basicConfig(filename = "/var/log/euromillon/message.log",
        level = logging.DEBUG,
        format = LOG_FORMAT)
    logger = logging.getLogger()

    try:
        with open(Lectura,newline='') as csvfile:
            csvreader = csv.reader(csvfile, delimiter=',')
            for row in csvreader:
                numeros.append(row)
    except FileNotFoundError:
        logger.error("No existe el fichero numeros.txt")

    return numeros