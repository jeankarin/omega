import MySQLdb
import json
import logging

class conexionDB:
    # Creamos la estructura del log
    LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
    logging.basicConfig(filename = "/opt/files/message.log",
        level = logging.DEBUG,
        format = LOG_FORMAT)
    logger = logging.getLogger()

    # Leemos los datos del fichero de conexión para preparar la conexión
    try:
        with open('/opt/app/settings.json','r') as file:
            config = json.load(file)
        dbserver = config['EUROMILLON']['DBSERVER']
        dbuser = config['EUROMILLON']['USERNAME']
        dbpassword = config['EUROMILLON']['PASSWORD']
        dbname = config['EUROMILLON']['DATABASE']

        # Intentamos realizar la conexión y sino registramos el error en el log
        try:
            conexion = MySQLdb.connect(dbserver,dbuser,dbpassword,dbname)
            cursor = conexion.cursor()
        except MySQLdb.Error:
            logger.error("Imposible conectar con el servidor MySQL despues del reinicio del contenedor")
    except IOError:
        logger.error("Imposible abrir el fichero settings.json")
    
    # Leemos los últimos 5 registros de la base de datos
    def lastregistry(self):
        self.__class__.cursor.execute("SELECT * FROM NUMEROS ORDER BY ID DESC LIMIT 5;")
        datos = self.__class__.cursor.fetchall()
        self.__class__.conexion.close
        
        return datos
    
    # Insertamos los datos en la base de datos
    # (Revisar porque no me acaba de convencer)
    def insertNumeros(self, sql_numeros):
        for i in range(len(sql_numeros)):
            try:
                self.__class__.cursor.execute(sql_numeros[i])
                self.__class__.conexion.commit()
            except:
                self.__class__.conexion.rollback()
                return 1
        
        self.__class__.conexion.close
        return 0
    
    # Insertamos los datos en la base de datos
    # (Revisar porque no me acaba de convencer)
    def insertMillones(self, sql_millones):
        for i in range (len(sql_millones)):
            try:
                self.__class__.cursor.execute(sql_millones[i])
                self.__class__.conexion.commit()
            except:
                self.__class__.conexion.rollback()
                return 1
        
        self.__class__.conexion.close
        return 0