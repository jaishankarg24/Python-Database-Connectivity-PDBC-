'''Write a python program to establish the connection with database and perform some deletion operation w.rt
 data available within the table and display the data of before deletion and after deletion on the console'''

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

def delete_record():
	try:
		
		my_con=mysql.connector.connect(host=host,port=port,user=user,password=password,database=database)
		print(f'Python program got connected to the database: {database}')

		my_cursor=my_con.cursor()
		print('cursor object got created which is pointing to table ')

		#select * from tablename
		sql_select_query="""select * from `Employee`""" 
		
		my_cursor.execute(sql_select_query)
		print('sql query got executed on the table')

		records=my_cursor.fetchall()
		print(records)
		print(type(records))
		print('The data available in the table before deletion')
		for record in records:
			print(f'Name: {record[0]}')
			print(f'Subject: {record[1]}')
			print(f'Location: {record[2]}')
			print()
		print(f'The number of rows within the table: {len(records)}')
		print('******************************************************************')

		#delete from tablename where column name=data
		sql_delete_query="""delete from `Employee` where `location`='mandya'""" 
		my_cursor.execute(sql_delete_query)
		my_con.commit()
		print(' data has been deleted from the table')
		print()
		print('******************************************************************')

		sql_select_query="""select * from `Employee`""" 
		
		my_cursor.execute(sql_select_query)
		print('sql query got executed on the table')

		records=my_cursor.fetchall()
		print(records)
		print(type(records))
		print('The data available in the table after deletion')
		for record in records:
			print(f'Name: {record[0]}')
			print(f'Subject: {record[1]}')
			print(f'Location: {record[2]}')
			print()
		print(f'The number of rows within the table: {len(records)}')
		print('******************************************************************')

	except mysql.connector.Error as msg:
		print(f'The cause of the exception : {msg}')
	finally:
		close_connection(my_con,my_cursor)
if __name__ == '__main__':
	delete_record()


