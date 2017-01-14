#!/usr/bin/python
#-*-coding:latin-1-*-

#importamos nuestras librerias
import connection
import consultas

def ConsultaUltimos():
	con = connection.Connect()
	con.cursor()

	consulta = consultas.ConsultaFinal()

	con.executerins(consulta)
	
	con.close
