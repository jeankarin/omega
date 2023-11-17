import random

def generar_numeros_aleatorios_ordenados_sin_repeticion(numeros_generados=[], cantidad_numeros=5):
    if len(numeros_generados) == cantidad_numeros:
        numeros_generados.sort()
        return numeros_generados
    else:
        if cantidad_numeros == 2:
            nuevo_numero = random.randint(1,12)
        else:
            nuevo_numero = random.randint(1, 50)
        if nuevo_numero in numeros_generados:
            return generar_numeros_aleatorios_ordenados_sin_repeticion(numeros_generados, cantidad_numeros)
        else:
            numeros_generados.append(nuevo_numero)
            return generar_numeros_aleatorios_ordenados_sin_repeticion(numeros_generados, cantidad_numeros)

# Ejemplo de uso:
cantidad_numeros = int(input("Ingrese la cantidad de números aleatorios que desea generar: "))
numeros_aleatorios = generar_numeros_aleatorios_ordenados_sin_repeticion(cantidad_numeros=cantidad_numeros)
print(numeros_aleatorios)
