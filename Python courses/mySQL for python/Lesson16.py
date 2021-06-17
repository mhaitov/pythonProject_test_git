### python for mySQL

import mysql.connector

DB_LOGIN = 'root'
DB_PASS = 'marian96'

connection = mysql.connector.connect(host='localhost', user=DB_LOGIN, passwd=DB_PASS, database='testdb')

cursor = connection.cursor()
# #
# # cursor.execute("CREATE DATABASE")
# # for db in cursor:
# #     print(db)
#
# cursor.execute('SHOW TABLE')
#
# sql_query = "INSERT INTO students (name, surname, age) VALUES (%s, %s, %s)"
# # student = ('Jack', 'Smith', 30)
# student = [('Jack', 'Smith', 30), ('John', 'Brown', 25), ('Mary', 'Gold', 21), ('Barack', 'Obama' 65)]
#
#
# cursor.execute(sql_query, student)
# connection.comit()

cursor.execute('SELECT * FROM students')

student_data = cursor.fetchall()

cursor.execute('SELECT name FROM students WHERE name = %s', ("Mary",))
# for x in student_data:
#     print(x)
# for y in cursor:
#     print(y)
#
data = cursor.fetchall()

for x in data:
    print(x)
