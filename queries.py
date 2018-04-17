"""
Consultas SQL
"""

def ConsultaFinal():
	sql = ("""SELECT * FROM NUMEROS ORDER BY ID DESC LIMIT 10""")
	return sql

def InsertOne(num):
	sql = ("""INSERT INTO NUMEROS VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""" % (num[0], num[1], num[2], num[3], num[4], num[5], num[6], num[7], num[8], num[9], num[10]))
	return sql