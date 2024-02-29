import logging

def datos(numeros):
    LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
    logging.basicConfig(filename="/opt/files/message.log", level=logging.DEBUG, format=LOG_FORMAT)
    logger = logging.getLogger()

    meses = {'Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'}
    semana = {'Martes', 'Viernes'}
    error_count = 0

    # Comprobamos si los días de la semana y los meses están correctos.
    for row in numeros:
        if row[7] not in semana or row[9] not in meses:
            error_count += 1

    # Comprobamos que los 5 primeros números sean iguales o inferiores a 50.
    for row in numeros:
        if any(int(num) > 50 or int(num) == 0 for num in row[:5]):
            logger.error("check_file.py: Al menos uno de los primeros 5 números es mayor de 50 o igual a 0.")
            error_count += 1
    
    # Comprobamos si las estrellas son superiores a 12.
    for row in numeros:
        if int(row[5]) > 12 or int(row[6]) > 12:
            logger.error("check_file.py: Las estrellas no son correctas.")
            error_count += 1
    
    """
    # Comprobamos que el millón tiene 10 caracteres (8 + comillas).
    for row in numeros:
        if len(row[11]) != 10:
            logger.error
