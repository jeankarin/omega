import csv
import logging

def LecturaFichero(Lectura):

    # Variables y rutas
    FILE_LOG="message.log"
    numeros = []

    LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
    logging.basicConfig(filename="message.log",
                        level=logging.DEBUG,
                        format=LOG_FORMAT)
    logger = logging.getLogger()

    try:
        with open(Lectura, newline='') as csvfile:
            csvreader = csv.reader(csvfile, delimiter=',')
            for row in csvreader:
                numeros.append(row)
    except FileNotFoundError:
        logger.error("leer_fichero.py: No existe el fichero numeros.txt o lastregistry.txt")
        return 1
    
    return numeros