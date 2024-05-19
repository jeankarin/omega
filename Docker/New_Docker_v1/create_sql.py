def sql_format1(fichero):
    sql_query = []

    for i in range(len(fichero)):
        sql_query.append("""INSERT INTO NUMEROS VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""" % ('NULL', fichero[i][0], fichero[i][1], fichero[i][2], fichero[i][3], fichero[i][4], fichero[i][5], fichero[i][6], fichero[i][7], fichero[i][8], fichero[i][9], fichero[i][10]))

    return sql_query

def sql_format2(fichero,ultimoID):
    sql_millones = []

    for i in range(len(fichero)):
        ultimoID = int(ultimoID) + 1
        sql_millones.append("""INSERT INTO MILLONES VALUES (%s,%s,%s)""" % ('NULL',fichero[i][11],ultimoID))
    
    return sql_millones

def ultimo_ID():
    sql_ultimoid = ("""SELECT * FROM NUMEROS ORDER BY ID DESC LIMIT 5""")

    return sql_ultimoid