def sql_format1(fichero):
    sql_query = [
        """INSERT INTO NUMEROS VALUES (NULL, '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')""" % tuple(row[:11])
        for row in fichero
    ]
    return sql_query

def sql_format2(fichero, ultimoID):
    sql_millones = [
        """INSERT INTO MILLONES VALUES (NULL, '%s', '%s')""" % (row[11], ultimoID)
        for row in fichero
    ]
    return sql_millones

def ultimo_ID():
    sql_ultimoid = """SELECT * FROM NUMEROS ORDER BY ID DESC LIMIT 5"""
    return sql_ultimoid
