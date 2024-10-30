import logging

def datos(numeros):
	
	# Variables y RUTAS (CAMBIAR RUTAS EN PRODUCCION)
	FILE_LOG="message.log"
	meses = {'Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'}
	semana = {'Martes', 'Viernes'}
	error_count = 0
	
	LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
	logging.basicConfig(filename=FILE_LOG, level=logging.DEBUG, format=LOG_FORMAT)
	logger = logging.getLogger()

    # Comprobamos si los dias de la semana están correctos
	for row in numeros:
		if row[7] not in semana:
			logger.error("check_file.py: Error en los dias de la semana")
			error_count += 1
	
	# Comprobamos si los meses de la semana están correctos
	for row in numeros:
		if row[9] not in meses:
			logger.error("check_file.py: Error en los meses")
			error_count += 1
	
	# Comprobamos que los 5 primeros números sean inferiores a 50.
	for row in numeros:
		if any(int(num) > 50 or int(num) == 0 for num in row[:5]):
			logger.error("check_file.py: Numeros incorrectos, igual a 0 o mayor a 50")
			error_count += 1
	
	# Comprobamos si las estrellas son superiores a 12 o igual a 0:
	for row in numeros:
		if any(int(num) > 12 or int(num) == 0 for num in row[5:7]):
			logger.error("check_file.py: Los números de las estrellas son incorrectos")
			error_count += 1
	
	# Comprobamos que el millon tenga 8 carácteres
	for row in numeros:
		if len(row[11]) != 8:
			logger.error("check_file.py: Los millones no son correctos")
			error_count += 1 
	
	return error_count