#!/usr/bin/python
#-*-coding:latin-1-*-

#consultas predefinidas en la db

def ConsNum01All():
	sql = (""" SELECT num01 FROM numeros""") #Mustra todos los numeros de la primera columna
	return sql

def ConsNum02All():
	sql = (""" SELECT num02 FROM numeros""") #Mustra todos los numeros de la segunda columna
	return sql

def ConsNum03All():
	sql = (""" SELECT num03 FROM numeros""") #Mustra todos los numeros de la tercera columna
	return sql

def ConsNum04All():
	sql = (""" SELECT num04 FROM numeros""") #Mustra todos los numeros de la cuarta columna
	return sql

def ConsNum05All():
	sql = (""" SELECT num05 FROM numeros""") #Mustra todos los numeros de la quinta columna
	return sql

def ConsStar01All():
	sql = (""" SELECT star01 FROM numeros""") #Mustra todos los numeros de la sexta columna
	return sql

def ConsStar02All():
	sql = (""" SELECT star02 FROM numeros""") #Mustra todos los numeros de la septima columna
	return sql