"""
Fichero principal para ejecutar la aplicación
"""

# Importamos los ficheros y librerías necesarias
import time # Para hacer que se espere y no esté consultado siempre si la carpeta tiene el fichero numeros.txt
import sql_connection # Función de conexión al servidor MySQL
import lectura_fichero # Función para leer fichero csv
import sql_querys # Función para generar las querys
import os # Para cargar comandos del sistema y borrar los ficheros txt después de usarlos
import logging_class # Al final hemos creado una clase para gestionar los errores del log
import ficheros_necesarios # Aquí se crean los ficheros necesarios 

def main():
    temp = 0
    ficheros_necesarios.newFiles() #Creamos los ficheros si no existen.
    ficheros_necesarios.lastRegistryFile(temp) # Generamos fichero con los últimos 5 registros
    registro = logging_class.checkError()

    # Ejecutamos aplicación princial
    if (os.path.exists("/home/jeankarin/DevLocal/git/omega/Docker/Temporal/Linux/files/numeros.txt")):

        # Conseguimos el último ID del fichero si existe o creamos el fichero si no existe
        ultimoID_temp = lectura_fichero.lecturaFichero('/home/jeankarin/DevLocal/git/omega/Docker/Temporal/Linux/files/lastregistry.txt')
        #print(type(ultimoID_temp))
        ultimoID = ultimoID_temp[0][0][1::]

        # Leemos el fichero numeros.txt
        numeros = lectura_fichero.lecturaFichero('/home/jeankarin/DevLocal/git/omega/Docker/Temporal/Linux/files/numeros.txt')

        # Comprobamos que el fichero tenga la información correcta
        error = 0
        error = lectura_fichero.checkErrorFile(numeros)

        if error > 0:
            os.system("mv /home/jeankarin/DevLocal/git/omega/Docker/Temporal/Linux/files/numeros.txt /home/jeankarin/DevLocal/git/omega/Docker/Temporal/Linux/files/numeros_error.txt")
            pass # No salimos porque no debería seguir ejecutando porque no existe el fichero numeros.txt
        else:
            # Montamos las querys con la información e iniciamos un insert con los datos.
            sql_numeros = sql_querys.numerosSQL(numeros)
            sql_millones = sql_querys.millonesSQL(numeros, ultimoID)
            miConexion = sql_connection.conexionDB()
            result1 = miConexion.insertNumeros(sql_numeros)
            miConexion2 = sql_connection.conexionDB()
            result2 = miConexion2.insertMillones(sql_millones)

            # Borramos el fichero si todo ha ido bien
            if (result1 == 0) and (result2 == 0):
                registro.successUpdate()
                os.system("rm /home/jeankarin/DevLocal/git/omega/Docker/Temporal/Linux/files/numeros.txt")
                # Falta actualizar el fichero lastregistry con los nuevos datos.
                temp = 1
                ficheros_necesarios.lastRegistryFile(temp)
            else:
                registro.errorUpdate()

if __name__ == '__main__':
    main()