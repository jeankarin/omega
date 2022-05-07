## -- Funcion principal -- ##
def main():

	# Create and configure logger
	LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
	logging.basicConfig(filename = "/var/log/euromillon/message.log",
		level = logging.DEBUG,
		format = LOG_FORMAT)

	logger = logging.getLogger()

	# Start the bucle
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
						logger.info("Base de datos actualizada correctamente")

						## -- Borramos ficheros -- ##
						os.system("rm /opt/files/numeros.txt")
						os.system("rm /opt/files/millones.txt")
						if (os.path.isfile("/opt/files/numeros.txt") and os.path.isfile("/opt/files/numeros_.txt")):
							logger.warning("Ficheros no borrados")
						else:
							logger.info("Ficheros borrados")
					else:
						logger.error("numeros.txt esta mal")
						## -- Borramos ficheros -- ##
						os.system("mv /opt/files/numeros.txt /opt/files/numeros_.txt")
						os.system("mv /opt/files/millones.txt /opt/files/millones_.txt")
				else:
					logger.error("millones.txt esta mal")
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
	import logging
	main()
