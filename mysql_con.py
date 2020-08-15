import MySQLdb
import json
from tqdm import tqdm

def InsertData(sql):
	with open('settings.json', 'r') as file:
		config = json.load(file)

	dbserver = config['EUROMILLON']['DBSERVER']
	dbuser = config['EUROMILLON']['USERNAME']
	dbpassword = config['EUROMILLON']['PASSWORD']
	dbname = config['EUROMILLON']['DATABASE']

	con = MySQLdb.connect(dbserver,dbuser,dbpassword,dbname)
	cur = con.cursor()

	for i in tqdm(range(len(sql))):
		try:
			cur.execute(sql[i])
			con.commit()
		except:
			con.rollback()
			print("Hay algun error, ejecutamos rollback")

	con.close()
