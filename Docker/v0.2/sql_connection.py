import MySQLdb
import json
import logging

class conexionDB:
    LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
    logging.basicConfig(filename = "/opt/files/message.log",
        level = logging.DEBUG,
        format = LOG_FORMAT)
    logger = logging.getLogger()

    try:
        with open('/opt/app/settings.json','r') as file:
            config = json.load(file)
        dbserver = config['EUROMILLON']['DBSERVER']
        dbuser = config['EUROMILLON']['USERNAME']
        dbpassword = config['EUROMILLON']['PASSWORD']
        dbname = config['EUROMILLON']['DATABASE']

        try:
            conexion = MySQLdb.connect(dbserver,dbuser,dbpassword,dbname)
            cursor = conexion.cursor()
        except MySQLdb.Error:
            logger.error("Imposible conectar con el servidor MySQL despues del reinicio del contenedor")
    except IOError:
        logger.error("Imposible abrir el fichero settings.json")