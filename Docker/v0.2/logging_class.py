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
    
    def lecturaFichero(self):
        self.logger.error("Lectura fichero: No existe el fichero numeros.txt ó error leyendo el fichero")
    
    def errorNum(self,num):
        if (num == 1):
            self.logger.error("Error en numeros.txt Día mal indicado.")
        elif (num == 2):
            self.logger.error("Error en numeros.txt Mes mal indicado.")
        elif (num == 3):
            self.logger.error("Error en numeros.txt Millon mal indicado.")
        elif (num == 4):
            self.logger.error("El fichero numeros.txt está mal creado")
    
    def errorMySQL(self,num):
        if (num == 1):
            self.logger.error("Imposible conectar con el servidor MySQL despues del reinicio del contenedor")
        elif (num == 2):
            self.logger.error("Imposible abrir el fichero settings.json")
        elif (num == 3):
            self.logger.error("Servidor MySQL no disponible")