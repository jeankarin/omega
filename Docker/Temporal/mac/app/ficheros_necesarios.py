"""
Funciones para la creación de ficheros y cosas generales necesarias.
"""

import os
import sql_connection

# Poblamos el fichero con la información necesaria
def lastRegistryFile(temp):
    tempID = 0
    if (os.stat("~/DevLocal/git/omega/Docker/Temporal/mac/files/lastregistry.txt").st_size == 0) or (temp > 0):
        miConexion = sql_connection.conexionDB()
        tempID = miConexion.lastregistry()

        # Escribimos los registros en el fichero.
        with open("~/DevLocal/git/omega/Docker/Temporal/mac/files/lastregistry.txt", "w") as file:
            for i in range(len(tempID)):
                file.write(str(tempID[i]) + "\n")
        
        file.close()

# Creamos los ficheros necesarios.
def newFiles():
    temp = 0
    if (os.path.isfile("~/DevLocal/git/omega/Docker/Temporal/mac/files/message.log") == False):
        os.system("touch ~/DevLocal/git/omega/Docker/Temporal/mac/files/message.log")
    if (os.path.isfile("~/DevLocal/git/omega/Docker/Temporal/mac/files/lastregistry.txt") == False):
        os.system("touch ~/DevLocal/git/omega/Docker/Temporal/mac/files/lastregistry.txt")
    
    if (os.path.exists("~/DevLocal/git/omega/Docker/Temporal/mac/files/lastregistry.txt")) == True:
        lastRegistryFile(temp)