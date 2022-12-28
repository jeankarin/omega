def main():
    ###Creamos el fichero de log
    comprobar.createLog()
    
    ###Leemos el fichero
    fichero = leerfichero.LecturaFichero('/opt/files/numeros.txt')

if __name__ == '__main__':
    import leerfichero
    import comprobar
    main()