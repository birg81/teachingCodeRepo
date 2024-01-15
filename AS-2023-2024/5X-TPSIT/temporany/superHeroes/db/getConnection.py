import mysql.connector as dbms

def getConnection():
	return dbms.connect(
		host = 'localhost',
		port = 3306,
		user = 'root',
		password = '',
		database = 'NeapolitansSuperHeroesDB'
	)