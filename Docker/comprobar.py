import logging

#Fichero de Logs
def checkErrorsLogs():
    #Comprobamos si el fichero de logs existe
    try:
        with open('/var/log/euromillon/message.log') as file:
            file.close()
    except (FileNotFoundError, PermissionError):
        print("Registro no creado en /var/log/euromillon/message.log")
        exit()

def checkErrorFile(numeros):
    LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
    logging.basicConfig(filename = "/var/log/euromillon/message.log",
        level = logging.DEBUG,
        format = LOG_FORMAT)
    logger = logging.getLogger()

    for i in len(numeros):
        if (numeros[i][8] != "Martes") or (numeros[i][8] != "Viernes"):
            logger.error("Error en numeros.txt Día indicado incorrecto debe ser Martes o Viernes")

