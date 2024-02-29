import os
import time
import gc
import logging_class
import leerfichero
import check_file
import create_sql
import ficheros_necesarios
import sql_connection

def main():
    registro = logging_class.checkError()

    # Creamos los ficheros necesarios.
    ficheros_necesarios.newFiles()

    # Repetimos el bucle infinitamente.
    while True:
        # Comprobamos si el fichero existe para leerlo.
        if os.path.exists("/opt/files/numeros.txt"):
            fichero = leerfichero.LecturaFichero('/opt/files/numeros.txt')
            ultimoID_temp = leerfichero.LecturaFichero('/opt/files/lastregistry.txt')
            if fichero == 1 or ultimoID_temp == 1:
                break

            ultimoID = ultimoID_temp[0][0][1::]
            datos = check_file.datos(fichero)

            if datos == 1:
                os.system("mv /opt/files/numeros.txt /opt/files/numeros_error.txt")
                break

            sql_numeros = create_sql.sql_format1(fichero)
            sql_millones = create_sql.sql_format2(fichero, ultimoID)
            with sql_connection.conexionDB() as miConexion, sql_connection.conexionDB() as miConexion2:
                result1 = miConexion.insertNumeros(sql_numeros)
                result2 = miConexion2.insertMillones(sql_millones)

            if result1 == 0 and result2 == 0:
                registro.successUpdate()
                os.system("rm /opt/files/numeros.txt")
                temp = 1
                ficheros_necesarios.lastRegistryFile(temp)
            else:
                registro.errorUpdate()

            del fichero, ultimoID_temp, ultimoID, datos, sql_numeros, sql_millones, miConexion, miConexion2, result1, result2, temp
            gc.collect()
        else:
            time.sleep(5)

if __name__ == '__main__':
    main()
