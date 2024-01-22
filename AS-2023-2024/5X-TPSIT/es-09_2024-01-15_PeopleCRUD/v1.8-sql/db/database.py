#import mysql.connector as dbms
import sqlite3 as dbms
from entity.Person import Person

def getConnection():
	# return dbms.connect(host = 'localhost', port = 3306, user = 'root', password = '', database = 'PeopleDB')
	return dbms.connect('PeopleDB.db')

def selectFromTab(condition:str = ''):
	condition = f'WHERE {condition}' if condition else ''
	q = 'SELECT id, firstname, lastname, age FROM People {} ORDER BY lastname;'.format(condition)
	con = getConnection()
	if con:
		try:
			cur = con.cursor()
			cur.execute(q)
			rs = cur.fetchall()
			if len(rs) > 0:
				return [
					Person (
						id = p[0],
						firstname = p[1],
						lastname = p[2],
						age = p[3]
					)
					for p in rs
				]
			else:
				return []
		finally:
			cur.close()
			con.close()
	else:
		return []

def updateFromTab(q:str):
	con = getConnection()
	if con:
		try:
			cur = con.cursor()
			cur.execute(q)
			con.commit()
			return cur.rowcount
		finally:
			cur.close()
			con.close()
	else:
		return -1