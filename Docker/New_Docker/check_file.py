''' Revisamos la información si es correcta y si lo es
creamos la estructura sql '''

import logging

def datos(numeros):

    LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
    logging.basicConfig(filename = "/opt/files/message.log",
        level = logging.DEBUG,
        format = LOG_FORMAT)
    logger = logging.getLogger()

    meses = ['Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre']
    semana = ['Martes','Viernes']
    error1 = 0

    # Comprobamos si los días de la semana y los meses están bien.
    for i in range (len(numeros)):
        if str(numeros[i][7]) not in str(semana):
            error1 += 1
        if str(numeros[i][9]) not in str(meses):
            error1 += 1
    
    # Comprobamos que los 5 primeros números sean iguales ó inferiores a 50.
    for i in range (len(numeros)):
        for x in range(0,5):
            if int(numeros[i][x]) > 50 or int(numeros[i][x]) == 0:
                logger.error("check_file.py: De los 5 primeros numeros, 1 es mayor de 50 o igual a 0.")
                error1 += 1
    
    # Comprobamos si las estrellas son superiores a 12.
    for i in range (len(numeros)):
        if (int(numeros[i][5]) > 12) or (int(numeros[i][6]) > 12):
            logger.error("check_file.py: Las estrellas no están correctas.")
            error1 += 1
    
    """ # Comprobar que el millon es de 10 carácteres. 8 más las comillas (')
    for i in range (len(numeros)):
        num = len(numeros[i][11])
        if  num != 10:
            logger.error("check_file.py: Los millones no están correctos.")
            error1 += 1
    """
    
    # Si ha sumado algún error lo registramos en el log.
    if error1 > 0:
        logger.error("check_file.py: Los datos leídos del txt no son correctos.")
        return 1
    else:
        return 0