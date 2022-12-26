import logging

def checkfile(fichero):
    # Configuramos estructura del log.
    errores = 0

    LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
    logging.basicConfig(filename = "/var/log/euromillon/message.log",
        level = logging.DEBUG,
        format = LOG_FORMAT)

    print("Hola")

    return errores