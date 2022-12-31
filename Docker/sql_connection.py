import MySQLdb
import json

class conexionDB:
    with open('/opt/app/settings.json', 'r') as file:
        config = json.load(file)

    dbserver = config['EUROMILLON']['DBSERVER']
    dbuser = config['EUROMILLON']['USERNAME']
    dbpassword = config['EUROMILLON']['PASSWORD']
    dbname = config['EUROMILLON']['DATABASE']

    conexion = MySQLdb.connect(dbserver,dbuser,dbpassword,dbname)
    cursor = conexion.cursor()

    def ultimoID(self):
        self.__class__.cursor.execute("SELECT * FROM NUMEROS;")
        data = self.__class__.cursor.fetchall()
        ultimoID = data[len(data)-1][0]
        
        return ultimoID
    
    def insertNumeros(self,sql_numeros):
        for i in range(len(sql_numeros)):
            try:
                self.__class__.cursor.execute(sql_numeros[i])
                self.__class__.conexion.commit()
                self.__class__.conexion.close
                return 0
            except:
                self.__class__.conexion.rollback()
                return 1
    
    def insertMillones(self,sql_millones):
        for i in range(len(sql_millones)):
            try:
                self.__class__.cursor.execute(sql_millones[i])
                self.__class__.conexion.commit()
                self.__class__.conexion.close
                return 0
            except:
                self.__class__.conexion.rollback()
                return 1