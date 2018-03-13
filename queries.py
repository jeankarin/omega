"""
Consultas SQL
"""

def ConsultaFinal():
	sql = ("""SELECT * FROM NUMEROS ORDER BY ID DESC LIMIT 10""")
	return sql