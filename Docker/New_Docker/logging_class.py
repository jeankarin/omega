import logging

class checkError:
    LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
    logging.basicConfig(filename = "/opt/files/message.log",
        level = logging.DEBUG,
        format = LOG_FORMAT)
    logger = logging.getLogger()

    def successUpdate(self):
        self.logger.info("Base de datos actualizada correctamente")
    
    def errorUpdate(self):
        self.logger.info("Error actualizando la base de datos")

    def errorMySQL(self,num):
        if (num == 1):
            self.logger.error("Imposible conectar con el servidor MySQL despues del reinicio del contenedor")
        elif (num == 2):
            self.logger.error("Imposible abrir el fichero settings.json")
        elif (num == 3):
            self.logger.error("Servidor MySQL no disponible")