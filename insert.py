#!/usr/bin/python
#-*-coding:latin-1-*-

#importamos nuestras librerias
import connection
import consultas

def Insert_to_database(num):
	con = connection.Connect()
	con.cursor()

	consulta = consultas.InsertNum(num)

	con.executerins(consulta)
	
	con.close
