#!/usr/bin/python
#-*-coding:latin-1-*-

def InsertNum(num):
	sql = ("""CALL PA_INSERT_NUMERO(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""" % (num[0], num[1], num[2], num[3], num[4], num[5], num[6], num[7], num[8], num[9], num[10], num[11]))
	return sql

def ConsultaFinal():
	sql = ("""SELECT NUM01,NUM02,NUM03,NUM04,NUM05,STAR01,STAR02,DIASEM,DIA,MES,ANYO,MILLON FROM NUMEROS WHERE ANYO = 2017 ORDER BY ID DESC LIMIT 10""")
	return sql
