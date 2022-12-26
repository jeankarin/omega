def main():
    ###Leemos el fichero
    fichero = leerfichero.LecturaFichero('numeros.txt')
    
    ###Realizamos la comprovación del fichero
    errores = comprobar.checkfile(fichero)

if __name__ == '__main__':
    import leerfichero
    import comprobar
    main()