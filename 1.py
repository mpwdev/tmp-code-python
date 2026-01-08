import sqlite3
connection = sqlite3.connect('my_db01.db')

cursor = connection.cursor()

id = input('Enter an ID: ')

sql = 'UPDATE employees SET phone="123123" where id = ?'

cursor.execute(sql, (id,))

connection.commit()

connection.close()