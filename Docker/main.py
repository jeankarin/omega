def main():
    ###Creamos el fichero de log
    comprobar.checkErrorsLogs()

    ###Leemos el fichero
    numeros = leerfichero.LecturaFichero('/opt/files/numeros.txt')

if __name__ == '__main__':
    import leerfichero
    import comprobar
    main()