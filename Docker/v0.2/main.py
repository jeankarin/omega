"""
Fichero principal para ejecutar la aplicación
"""

# Poblamos el fichero con la información necesaria
def lastRegistryFile():
    tempID = 0
    if (os.stat("/opt/files/lastregistry.txt").st_size == 0):
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

def main():
    newFiles() # Creamos los ficheros si no existen.
    lastRegistryFile() # Generamos fichero con los últimos 5 registros

    # Ejecutamos aplicación princial
    while True:
        if (os.path.exists("/opt/files/numeros.txt")):

            # Conseguimos el último ID del fichero si existe o creamos el fichero si no existe
            ultimoID_temp = lectura_fichero.lecturaFichero('/opt/files/lastregistry.txt')
            ultimoID = ultimoID_temp[1::]
            print(ultimoID)

            # Leemos el fichero numeros.txt
            numeros = lectura_fichero.lecturaFichero('/opt/files/numeros.txt')

            # Comprobamos que el fichero tenga la información correcta
            error = 0

            error = lectura_fichero.checkErrorFile(numeros)
            if error > 0:
                os.system("mv /opt/files/numeros.txt /opt/files/numeros_error.txt")
                pass # No salimos porque no debería seguir ejecutando porque no existe el fichero numeros.txt
            else:
                sql_numeros = sql_querys.numerosSQL(numeros)
        else:
            time.sleep(5)

if __name__ == '__main__':
    import time # Para hacer que se espere y no esté consultado siempre si la carpeta tiene el fichero numeros.txt
    import sql_connection # Función de conexión al servidor MySQL
    import lectura_fichero # Función para leer fichero csv
    import sql_querys # Función para generar las querys
    import os # Para cargar comandos del sistema y borrar los ficheros txt después de usarlos

    main()