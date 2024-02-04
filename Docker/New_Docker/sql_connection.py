import MySQLdb
import json
import os
import time
import logging_class

class conexionDB:

    # Hacemos ping al servidor
    num = os.system("ping -c2 -q -i5 192.168.1.41")
    logError1 = logging_class.checkError()

    # Leemos los datos del fichero de conexión para preparar la conexión
    if num == 0:
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
                logError1.errorMySQL(1)
        except IOError:
            logError1.errorMySQL(2)
    else:
        logError1.errorMySQL(3)
        time.sleep(30) # Esperamos 30 segundos a que se inicie el contenedor del MySQL
    
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