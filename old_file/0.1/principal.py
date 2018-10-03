#!/usr/bin/python

def lecFichero():
    fichero = open('numeros.txt','r')
    fichero.seek(0)
    tamanio=len(fichero.readlines())
    fichero.close()
    return tamanio

def main():
    FILEN = lecFichero()
    print(FILEN)

    for x in tqdm(range(FILEN)):
        print("Hola")

if __name__ == '__main__':
    from tqdm import tqdm
    main()
