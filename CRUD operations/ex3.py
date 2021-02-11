''' Write a python program to establish the connection with database and insert/create multiple 
 records/data within the table'''

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

def insert_multiple_records():
	try:
		
		my_con=mysql.connector.connect(host=host,port=port,user=user,password=password,database=database)
		print(f'Python program got connected to the database: {database}')

		my_cursor=my_con.cursor()
		print('cursor object got created which is pointing to table ')

		#insert into tablename(column names) values(data/record)
		sql_insertmany_query="""insert into `Employee`(`name`,`subject`,`location`) values(%s,%s,%s)""" 
		records=[('sandesh','python','mysore'),('kiran','angular','mandya'),('somanna','java','coorg')]

		my_cursor.executemany(sql_insertmany_query,records)
		print('sql query got executed on the table')

		my_con.commit()
		print('changes made within the table got commited in the database')

		print(f'a record got inserted within :{database} database')

	except mysql.connector.Error as msg:
		print(f'The cause of the exception : {msg}')
	finally:
		close_connection(my_con,my_cursor)
if __name__ == '__main__':
	insert_multiple_records()

