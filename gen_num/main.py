### Generamos num1eros para el sorteo

## Generación de numeros
def numgen(millon):
    num1 = []
    if ( millon != 2 ):
        rep = 51
    else:
        rep = 12
    
    while len(num1) < millon:
        ran = random.randrange(1,rep)
        if (ran in num1):
            pass
        else:
            num1.append(ran)
    
    return num1

## Funcion principal
def main():
    num1 = []

    num1 = numgen(5)
    num1.sort()
    print(num1)
    num1 = numgen(2)
    num1.sort()
    print(num1)

if __name__ == '__main__':
    import random
    main()