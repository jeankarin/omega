#!/usr/bin/python
#-*-coding:latin-1-*-

#importamos nuestras librerias
import con_db
import cons

def extract_num(num):
	#Create the cursor to database
	con = con_db.Connect()
	con.cursor()

	if (num == 1):
		#Input num to search
		consulta = cons.ConsNum01All()

	if (num == 2):
		#Input num to search
		consulta = cons.ConsNum02All()

	if (num == 3):
		#Input num to search
		consulta = cons.ConsNum03All()

	if (num == 4):
		#Input num to search
		consulta = cons.ConsNum04All()

	if (num == 5):
		#Input num to search
		consulta = cons.ConsNum05All()

	if (num == 6):
		#Input num to search
		consulta = cons.ConsStar01All()

	if (num == 7):
		#Input num to search
		consulta = cons.ConsStar02All()

	#Execute the query
	con.executer (consulta)

	#Cerramos la conexión con la db.
	con.close

