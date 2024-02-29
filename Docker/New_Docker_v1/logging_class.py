import logging

class CheckError:
    def __init__(self):
        # Configuración del registro de errores
        self.LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
        logging.basicConfig(filename="/opt/files/message.log",
                            level=logging.DEBUG,
                            format=self.LOG_FORMAT)
        self.logger = logging.getLogger()

    def successUpdate(self):
        self.logger.info("Base de datos actualizada correctamente")
    
    def errorUpdate(self):
        self.logger.info("Error actualizando la base de datos")

    def errorMySQL(self, num):
        error_messages = {
            1: "Imposible conectar con el servidor MySQL después del reinicio del contenedor",
            2: "Imposible abrir el fichero settings.json",
            3: "Servidor MySQL no disponible"
        }
        error_message = error_messages.get(num, "Error desconocido")
        self.logger.error(error_message)
