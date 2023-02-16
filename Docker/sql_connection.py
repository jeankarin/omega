import MySQLdb
import json
import comprobar_class

class conexionDB:
    with open('/opt/app/settings.json', 'r') as file:
        config = json.load(file)

    mySQLerror = comprobar_class.checkError()
    dbserver = config['EUROMILLON']['DBSERVER']
    dbuser = config['EUROMILLON']['USERNAME']
    dbpassword = config['EUROMILLON']['PASSWORD']
    dbname = config['EUROMILLON']['DATABASE']

    try:
        conexion = MySQLdb.connect(dbserver,dbuser,dbpassword,dbname)
        cursor = conexion.cursor()
    except MySQLdb.Error:
        mySQLerror.checkConnectionDB()

    def lastregistry(self):
        self.__class__.cursor.execute("SELECT * FROM NUMEROS ORDER BY ID DESC LIMIT 5;")
        datos = self.__class__.cursor.fetchall()
        self.__class__.conexion.close
        return datos
        
    def ultimoID(self):
        errorID = comprobar_class.checkError()
        ultimoID = ''

        try:
            self.__class__.cursor.execute("SELECT * FROM NUMEROS;")
            data = self.__class__.cursor.fetchall()
            ultimoID = data[len(data)-1][0]
        except AttributeError:
            errorID.checkSQLServer()
        except IndexError:
            errorID.ultimoIDError()
        
        if ultimoID == '' or self.__class__.conexion == '':
            return False
        else:
            self.__class__.conexion.close
            return ultimoID
    
    def insertNumeros(self,sql_numeros):
        for i in range(len(sql_numeros)):
            try:
                self.__class__.cursor.execute(sql_numeros[i])
                self.__class__.conexion.commit()
            except:
                self.__class__.conexion.rollback()
                return 1
        
        self.__class__.conexion.close
        return 0
    
    def insertMillones(self,sql_millones):
        for i in range(len(sql_millones)):
            try:
                self.__class__.cursor.execute(sql_millones[i])
                self.__class__.conexion.commit()
            except:
                self.__class__.conexion.rollback()
                return 1
        
        self.__class__.conexion.close
        return 0