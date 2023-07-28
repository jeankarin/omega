"""
Funciones para la creación de ficheros y cosas generales necesarias.
"""

import os
import sql_connection

# Poblamos el fichero con la información necesaria
def lastRegistryFile(temp):
    tempID = 0
    if (os.stat("/opt/files/lastregistry.txt").st_size == 0) or (temp > 0):
        miConexion = sql_connection.conexionDB()
        tempID = miConexion.lastregistry()

        # Escribimos los registros en el fichero.
        with open("/opt/files/lastregistry.txt", "w") as file:
            for i in range(len(tempID)):
                file.write(str(tempID[i]) + "\n")
        
        file.close()

# Creamos los ficheros necesarios.
def newFiles():
    if (os.path.isfile("/opt/files/message.log") == False):
        os.system("touch /opt/files/message.log")
    if (os.path.isfile("/opt/files/lastregistry.txt") == False):
        os.system("touch /opt/files/lastregistry.txt")
    
    if (os.path.exists("/opt/files/lastregistry.txt")) == True:
        lastRegistryFile()