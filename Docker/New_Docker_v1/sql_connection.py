import os
import MySQLdb
import json
import time
import logging_class

class ConexionDB:
    def __init__(self):
        self.logError1 = logging_class.CheckError()
        self.ping_server()

        try:
            with open('/opt/app/settings.json', 'r') as file:
                config = json.load(file)
            dbserver = config['EUROMILLON']['DBSERVER']
            dbuser = config['EUROMILLON']['USERNAME']
            dbpassword = config['EUROMILLON']['PASSWORD']
            dbname = config['EUROMILLON']['DATABASE']

            # Intentamos realizar la conexión y sino registramos el error en el log
            try:
                self.conexion = MySQLdb.connect(dbserver, dbuser, dbpassword, dbname)
                self.cursor = self.conexion.cursor()
            except MySQLdb.Error:
                self.logError1.errorMySQL(1)
        except IOError:
            self.logError1.errorMySQL(2)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if hasattr(self, 'conexion'):
            self.conexion.close()

    def ping_server(self):
        num = os.system("ping -c2 -q -i5 192.168.1.41")
        if num != 0:
            self.logError1.errorMySQL(3)
            time.sleep(30) # Esperamos 30 segundos a que se inicie el contenedor de MySQL

    # Leemos los últimos 5 registros de la base de datos
    def lastregistry(self):
        self.cursor.execute("SELECT * FROM NUMEROS ORDER BY ID DESC LIMIT 5;")
        datos = self.cursor.fetchall()
        return datos

    # Insertamos los datos en la base de datos
    def insertNumeros(self, sql_numeros):
        for sql in sql_numeros:
            try:
                self.cursor.execute(sql)
                self.conexion.commit()
            except MySQLdb.Error:
                self.conexion.rollback()
                return 1

        return 0

    # Insertamos los datos en la base de datos
    def insertMillones(self, sql_millones):
        for sql in sql_millones:
            try:
                self.cursor.execute(sql)
                self.conexion.commit()
            except MySQLdb.Error:
                self.conexion.rollback()
                return 1

        return 0
