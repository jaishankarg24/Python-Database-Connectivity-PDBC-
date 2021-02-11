# DELETE

import mysql.connector

host='localhost'
port=3306
user='root'
password='root123'
database='cricketerdetails'

def close_connection(my_con,my_cursor):
	if my_con.is_connected():
			my_cursor.close()
			print('cursor object is closed')
			my_con.close()
			print(f'connection got closed from the database: {database}')

def dynamic_delete_record():
	try:
		
		my_con=mysql.connector.connect(host=host,port=port,user=user,password=password,database=database)
		print(f'Python program got connected to the database: {database}')

		my_cursor=my_con.cursor()
		print('cursor object got created which is pointing to table ')


		sql_select_query="""select * from `cricketer`""" 
		
		my_cursor.execute(sql_select_query)
		print('sql query got executed on the table')

		records=my_cursor.fetchall()
		print(records)
		print(type(records))
		print('The data available with table')
		for record in records:
			print(f'Name: {record[0]}')
			print(f'Age: {record[1]}')
			print(f'Country Name: {record[2]}')
			print()
		print(f'The number of rows within the table: {len(records)}')
		print('******************************************************************')

		#delete from tablename where columnname=%s
		sql_delete_query="""delete from `cricketer` where `country`= %s""" 
		country=input('Enter the country name of the cricketer:\t')
		input_data=(country,)
		my_cursor.execute(sql_delete_query,input_data)
		my_con.commit()
		print('new data has been deleted from the table')
		print()

		print('******************************************************************')

		sql_select_query="""select * from `cricketer`""" 
		
		my_cursor.execute(sql_select_query)
		print('sql query got executed on the table')

		records=my_cursor.fetchall()
		print(records)
		print(type(records))
		print('The data available with table')
		for record in records:
			print(f'Name: {record[0]}')
			print(f'Age: {record[1]}')
			print(f'Country Name: {record[2]}')
			print()
		print(f'The number of rows within the table: {len(records)}')
		print('******************************************************************')

	except mysql.connector.Error as msg:
		print(f'The cause of the exception : {msg}')
	finally:
		close_connection(my_con,my_cursor)
if __name__ == '__main__':
	dynamic_delete_record()

