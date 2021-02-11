'''Write a python program to establish the connection with database and read/select a single
 record from the table'''
import mysql.connector

host='localhost'
port=3306
user='root'
password='root123'
database='employeedatabase'

def close_connection(my_con,my_cursor):
	if my_con.is_connected():
			my_cursor.close()
			print('cursor object is closed')
			my_con.close()
			print(f'connection got closed from the database: {database}')

def select_record():
	try:
		
		my_con=mysql.connector.connect(host=host,port=port,user=user,password=password,database=database)
		print(f'Python program got connected to the database: {database}')

		my_cursor=my_con.cursor()
		print('cursor object got created which is pointing to table ')

		#select * from tablename
		sql_select_query="""select * from `Employee`""" 
		
		my_cursor.execute(sql_select_query)
		print('sql query got executed on the table')

		record=my_cursor.fetchone()
		print(record)
		print(type(record))
		print('The data available with 1st row:')
		print(f'Name: {record[0]}')
		print(f'Subject: {record[1]}')
		print(f'Location: {record[2]}')

	except mysql.connector.Error as msg:
		print(f'The cause of the exception : {msg}')
	finally:
		close_connection(my_con,my_cursor)
if __name__ == '__main__':
	select_record()

