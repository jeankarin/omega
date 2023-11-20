"""
Funciones para la creación de ficheros y cosas generales necesarias.
"""

import os
import sql_connection

# Poblamos el fichero con la información necesaria
def lastRegistryFile(temp):
    tempID = 0
    if (os.stat("/home/jeankarin/DevLocal/git/omega/Docker/Temporal/Linux/files/lastregistry.txt").st_size == 0) or (temp > 0):
        miConexion = sql_connection.conexionDB()
        tempID = miConexion.lastregistry()

        # Escribimos los registros en el fichero.
        with open("/home/jeankarin/DevLocal/git/omega/Docker/Temporal/Linux/files/lastregistry.txt", "w") as file:
            for i in range(len(tempID)):
                file.write(str(tempID[i]) + "\n")
        
        file.close()

# Creamos los ficheros necesarios.
def newFiles():
    temp = 0
    if (os.path.isfile("/home/jeankarin/DevLocal/git/omega/Docker/Temporal/Linux/files/message.log") == False):
        os.system("touch /home/jeankarin/DevLocal/git/omega/Docker/Temporal/Linux/files/message.log")
    if (os.path.isfile("/home/jeankarin/DevLocal/git/omega/Docker/Temporal/Linux/files/lastregistry.txt") == False):
        os.system("touch /home/jeankarin/DevLocal/git/omega/Docker/Temporal/Linux/files/lastregistry.txt")
    
    if (os.path.exists("/home/jeankarin/DevLocal/git/omega/Docker/Temporal/Linux/files/lastregistry.txt")) == True:
        lastRegistryFile(temp)