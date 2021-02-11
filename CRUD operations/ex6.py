'''Write a python program to establish the connection with database and perform some updation w.rt data available within the table
and display the data of before updation and after updation on the console'''
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

def update_record():
	try:
		
		my_con=mysql.connector.connect(host=host,port=port,user=user,password=password,database=database)
		print(f'Python program got connected to the database: {database}')

		my_cursor=my_con.cursor()
		print('cursor object got created which is pointing to table ')

		#select * from tablename where columnname=data
		sql_select_query="""select * from `Employee` where `name`='kiran'""" 
		
		my_cursor.execute(sql_select_query)
		print('sql query got executed on the table')

		record=my_cursor.fetchone()
		print(record)
		print(type(record))
		print('The data before updation:')
		print(f'Name: {record[0]}')
		print(f'Subject: {record[1]}')
		print(f'Location: {record[2]}')
		print('******************************************************************')

		#update tablename set columnname=new data where columnname=old data
		sql_update_query="""update `Employee` set `name`='Kiran kumar P C' where `name`='kiran'""" 
		my_cursor.execute(sql_update_query)
		my_con.commit()
		print('new data has been updated within the table')
		print()
		print('******************************************************************')

		sql_select_query="""select * from `Employee` where `location`='mandya'""" 
		
		my_cursor.execute(sql_select_query)
		print('sql query got executed on the table')

		record=my_cursor.fetchone()
		print(record)
		print(type(record))
		print('The data after updation:')
		print(f'Name: {record[0]}')
		print(f'Subject: {record[1]}')
		print(f'Location: {record[2]}')

	except mysql.connector.Error as msg:
		print(f'The cause of the exception : {msg}')
	finally:
		close_connection(my_con,my_cursor)
if __name__ == '__main__':
	update_record()

