def SqlStatement(euro):
	sql = []
	sum = 0

	for i in range(len(euro)):
		if (euro[i][7] == "\'Martes\'") or (euro[i][7] == "\'Viernes\'"):
			sum = sum + 1

	if (sum == len(euro)):
		for i in range(len(euro)):
			sql.append("""INSERT INTO NUMEROS VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""" % ('NULL', euro[i][0], euro[i][1], euro[i][2], euro[i][3], euro[i][4], euro[i][5], euro[i][6], euro[i][7], euro[i][8], euro[i][9], euro[i][10]))
		return sql
	else:
		print ("Los datos del fichero numeros.csv no son correctos")
		print ("Detectados: " + str(sum) + "/" + str(len(euro)))
		return 0

def SqlStatement2(euro):
	sql = []

	for i in range(len(euro)):
		sql.append("""INSERT INTO MILLONES VALUES (%s,%s,%s)""" % ('NULL',euro[i][0],euro[i][1]))
	return sql
