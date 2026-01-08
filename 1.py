import sqlite3
connection = sqlite3.connect('my_db01.db')

cursor = connection.cursor()

sql = 'select * from employees;'

cursor.execute(sql)

for row in cursor.fetchall():
	print(row)

connection.close()