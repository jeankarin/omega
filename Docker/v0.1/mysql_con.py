import MySQLdb
import json

def InsertData(sql):
	with open('/opt/app/settings.json', 'r') as file:
		config = json.load(file)

	dbserver = config['EUROMILLON']['DBSERVER']
	dbuser = config['EUROMILLON']['USERNAME']
	dbpassword = config['EUROMILLON']['PASSWORD']
	dbname = config['EUROMILLON']['DATABASE']

	con = MySQLdb.connect(dbserver,dbuser,dbpassword,dbname)
	cur = con.cursor()

	for i in range(len(sql)):
		try:
			cur.execute(sql[i])
			con.commit()
		except:
			con.rollback()
			print("Hay algun error, ejecutamos rollback")

	con.close()