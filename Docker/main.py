def main():
    ###Creamos el fichero de log
    registro = comprobar_class.checkError()
    registro.checkErrorsLogs()

    while True:
        if (os.path.exists('/opt/files/numeros.txt')):
            ###Leemos el fichero
            numeros = leerfichero.LecturaFichero('/opt/files/numeros.txt')

            ###Variables para check
            error = 0
            ultimoID = 0

            ###Comprobamos errores en el fichero
            error = registro.checkErrorFile(numeros)
            if error > 0:
                os.system("mv /opt/files/numeros.txt /opt/files/numeros_error.txt")
                exit()
            else:
                sql_numeros = sql_querys.numerosSQL(numeros)
                miConexio = sql_connection.conexionDB()
                ultimoID = miConexio.ultimoID()
                if ultimoID == False:
                    exit()
                sql_millones = sql_querys.millonesSQL(numeros, ultimoID)
                result1 = miConexio.insertNumeros(sql_numeros)
                miConexio2 = sql_connection.conexionDB()
                time.sleep(5) # Dejamos 5 segundos porque parece que no inserta dos lineas seguidas, da error de conexión con la base de datos.
                result2 = miConexio2.insertMillones(sql_millones)
                if (result1 == 0) and (result2 == 0):
                    registro.successUpdate()
                    os.system('rm /opt/files/numeros.txt')
                else:
                    registro.errorUpdate()
        else:
            time.sleep(5)


if __name__ == '__main__':
    import time
    import sql_connection
    import leerfichero
    import comprobar_class
    import os
    import sql_querys

    main()
