def SqlStatement(euro):
	sql = []
	for i in range(len(euro)):
		sql.append("""INSERT INTO NUMEROS VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""" % ('NULL', euro[i][0], euro[i][1], euro[i][2], euro[i][3], euro[i][4], euro[i][5], euro[i][6], euro[i][7], euro[i][8], euro[i][9], euro[i][10]))
	return sql