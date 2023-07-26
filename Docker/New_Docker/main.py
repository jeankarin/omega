## Principal ##

def main():
	fichero = leerfichero.LecturaFichero('omega/Docker/New_Docker/numeros.txt') # Leemos el fichero
	datos = check_file.datos(fichero) # Comprobamos que algunos datos del fichero leido son correctos, ya añadiremos más
"""	if (datos == True):
		ultimoID = create_sql.ultimo_ID()
		if not ultimoID:
			print("Ultimo ID vacío")
		else:
			query_numeros = create_sql.sql_format1(fichero)
			query_millones = create_sql.sql_format2(fichero,ultimoID)
	
	if not query_numeros or not query_millones:
		print("La variable está vacía")
	else:
		print(query_numeros)
		print(query_millones)"""

if __name__ == '__main__':
	import leerfichero
	import check_file
	import create_sql
	main()