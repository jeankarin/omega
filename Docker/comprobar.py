import logging

def createLog():
    # Configuramos estructura del log.
    try:
        LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
        logging.basicConfig(filename = "/var/log/euromillon/message.log",
           level = logging.DEBUG,
           format = LOG_FORMAT)
    except FileNotFoundError:
        print("Registro no creado en /var/log/euromillon/message.log")
    except PermissionError:
        print("No tengo permisos para crear el fichero message.log")