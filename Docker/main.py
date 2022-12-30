def main():
    ###Variables para check
    error = 0

    ###Creamos el fichero de log
    comprobar.checkErrorsLogs()

    ###Leemos el fichero
    numeros = leerfichero.LecturaFichero('/opt/files/numeros.txt')
    ###Comprobamos errores en el fichero
    error = comprobar.checkErrorFile(numeros)
    if error > 0:
        os.system("mv /opt/files/numeros.txt /opt/files/numeros_error.txt")
        exit()
    else:
        sql_numeros = sql_querys.numerosSQL(numeros)
        # sql_millones = sql_querys.millonesSQL(numeros) !! FALTA SACAR EL ID DEL SORTEO PARA AÑADIR A MILLONES

if __name__ == '__main__':
    import leerfichero
    import comprobar
    import os
    import sql_querys
    main()