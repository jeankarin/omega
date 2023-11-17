"""
En este documento solo damos formato para realizar las consultas sql
"""

def numerosSQL(numeros):
    sql_query = []

    for i in range(len(numeros)):
        sql_query.append("""INSERT INTO NUMEROS VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""" % ('NULL', numeros[i][0], numeros[i][1], numeros[i][2], numeros[i][3], numeros[i][4], numeros[i][5], numeros[i][6], numeros[i][7], numeros[i][8], numeros[i][9], numeros[i][10]))
    
    return sql_query

def millonesSQL(numeros,ultimoID):
    sql_millones = []

    for i in range(len(numeros)):
        ultimoID = int(ultimoID) + 1
        sql_millones.append("""INSERT INTO MILLONES VALUES (%s,%s,%s)""" % ('NULL',numeros[i][11],ultimoID))
    
    return sql_millones