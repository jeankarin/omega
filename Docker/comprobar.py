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

    meses = ["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]
    dias = ["Martes","Viernes"]
    error = 0

    for i in range(len(numeros)):
        if (numeros[i][7] not in dias):
            logger.error("Error en numeros.txt Día mal indicado.")
            error += 1
        if (numeros[i][9] not in meses):
            logger.error("Error en numeros.txt Mes mal indicado.")
            error += 1
    
    return error