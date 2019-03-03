import pandas as pd
import MySQLdb

def hello():
	db = MySQLdb.connect(host="localhost",    # your host, usually localhost
	                     user="root",         # your username
	                     passwd="helloworld",  # your password
	                     db="hostel")        # name of the data base
	cur = db.cursor()
	cur.execute("select * from StudentInput;")
	arr = []
	for row in cur.fetchall():
	    arr.append(list(row))
	df = pd.DataFrame(arr)
	df.to_csv('sql.csv')
	df = df.transpose()

	val = df.values.tolist()
	db.close()
	return val
