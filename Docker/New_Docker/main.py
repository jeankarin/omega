## Principal ##

def main():
	# Variable necesarias
	start = False
	registro = logging_class.checkError()

	# Creamos los ficheros necesarios.
	ficheros_necesarios.newFiles()

	# Repetimos el bucle infinitamente.
	while not start:

		# Comprobamos si el fichero existe para leerlo.
		if (os.path.exists("/opt/files/numeros.txt")):
			# Leemos fichero
			fichero = leerfichero.LecturaFichero('/opt/files/numeros.txt')
			ultimoID_temp = leerfichero.LecturaFichero('/opt/files/lastregistry.txt')
			ultimoID = ultimoID_temp[0][0][1::]
			if (fichero == 1) or (ultimoID_temp == 1):
				start = True
			else:
				# Comprobamos que el fichero no contenga errores
				datos = check_file.datos(fichero)

				if datos == 1:
					os.system("mv /opt/files/numeros.txt /opt/files/numeros_error.txt")
					start = True
				else:
					# Montamos las querys para insertar en la base de datos
					sql_numeros = create_sql.sql_format1(fichero)
					sql_millones = create_sql.sql_format2(fichero,ultimoID)
					miConexion = sql_connection.conexionDB()
					result1 = miConexion.insertNumeros(sql_numeros)
					miConexion2 = sql_connection.conexionDB()
					result2 = miConexion2.insertMillones(sql_millones)

					# Borramos el fichero si todo ha ido bien
					if (result1 == 0) and (result2 == 0):
						registro.successUpdate()
						os.system("rm /opt/files/numeros.txt")
						# Actualizamos fichero Lastregistry.txt
						temp = 1
						ficheros_necesarios.lastRegistryFile(temp)
					else:
						registro.errorUpdate()
		else:
			time.sleep(5)

if __name__ == '__main__':
	import leerfichero
	import check_file
	import create_sql
	import ficheros_necesarios
	import logging_class
	import os
	import time
	import sql_connection
	main()