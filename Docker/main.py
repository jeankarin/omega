## -- Funcion principal -- ##
def main():
	try:
		TIME=True
		while TIME == True:
			## -- Comprovamos que existan los dos ficheros -- ##
			if (os.path.exists('/opt/files/numeros.txt') and os.path.exists('/opt/files/millones.txt')):
				
				## -- Leer fichero -- ##
				numeros = LecturaFichero('/opt/files/numeros.txt')
				millones = LecturaFichero('/opt/files/millones.txt')

				## -- Preparamos los sql para los inserts -- ##
				numsql = SqlNumeros (numeros)
				milsql = SqlMillones (millones)

				## -- Escribir base de datos -- ##
				if (numsql != 0):
					InsertData(numsql)
					InsertData(milsql)

				## -- Borramos ficheros -- ##
				os.system("rm /opt/files/numeros.txt")
				os.system("rm /opt/files/millones.txt")

			time.sleep(5)
			print("Esperando ficheros")
	except KeyboardInterrupt:
		print("Cancelado por el usuario")

if __name__ == '__main__':
	import time
	import os
	from lectura import LecturaFichero
	from sql_insert import *
	from mysql_con import *
	main()
