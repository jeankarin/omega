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
				# Variable resultado:
				resultado = 0
				resultado = confMillones(millones)
				if (resultado == 0):
					if (numsql != 0):
						InsertData(numsql)
						InsertData(milsql)

						## -- Borramos ficheros -- ##
						os.system("rm /opt/files/numeros.txt")
						os.system("rm /opt/files/millones.txt")
					else:
						print("numeros.txt esta mal")
						## -- Borramos ficheros -- ##
						os.system("mv /opt/files/numeros.txt /opt/files/numeros_.txt")
						os.system("mv /opt/files/millones.txt /opt/files/millones_.txt")
				else:
					print("millones.txt esta mal")
					## -- Borramos ficheros -- ##
					os.system("mv /opt/files/numeros.txt /opt/files/numeros_.txt")
					os.system("mv /opt/files/millones.txt /opt/files/millones_.txt")

			time.sleep(5)
	except KeyboardInterrupt:
		print("Cancelado por el usuario")

if __name__ == '__main__':
	import time
	import os
	from lectura import *
	from sql_insert import *
	from mysql_con import *
	main()
