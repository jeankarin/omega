import logging

class checkError:
    LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
    logging.basicConfig(filename = "/home/jeankarin/DevLocal/git/omega/Docker/Temporal/Linux/files/message.log",
        level = logging.DEBUG,
        format = LOG_FORMAT)
    logger = logging.getLogger()

    def successUpdate(self):
        self.logger.info("Base de datos actualizada correctamente")
    
    def errorUpdate(self):
        self.logger.info("Error actualizando la base de datos")