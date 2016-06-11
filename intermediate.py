#!/usr/bin/python
#-*-coding:latin-1-*-

#importamos nuestras librerias
import con_db
import cons

def extract_num():
	#Create the cursor to database
	con = con_db.Connect()
	con.cursor()

	#Input num to search
	consulta = cons.ConsNum01All()

	#Execute the query
	con.executer (consulta)

	#Cerramos la conexión con la db.
	con.close

