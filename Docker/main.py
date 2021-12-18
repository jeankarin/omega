#!/usr/bin/python

## -- Leer fichero -- ##

## -- Conectar MySQL -- ##

## -- Escribir fichero -- ##

## -- Funcion principal -- ##
def main():
	try:
		TIME=True
		while TIME == True:
			if os.path.exists('test.txt'):
				print("Fichero Existe")
			
			print ("Hola...")
			time.sleep(5)
	except KeyboardInterrupt:
		print("Cancelado por el usuario")


if __name__ == '__main__':
	import time
	import os
	main()