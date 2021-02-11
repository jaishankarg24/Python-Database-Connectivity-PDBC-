#dynamic create / insert operation
#multiple row

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

def dynamic_insert_multiple_records():
	try:
		
		my_con=mysql.connector.connect(host=host,port=port,user=user,password=password,database=database)
		print(f'Python program got connected to the database: {database}')

		my_cursor=my_con.cursor()
		print('cursor object got created which is pointing to table ')

		#insert into tablename(column names) values(data/record)
		sql_insert_query="""insert into `cricketer`(`name`,`age`,`country`) values(%s,%s,%s)""" 

		number=int(input('Enter the number of rows:\t'))
		for i in range(number):

			name=input('Enter the name of cricketer:\t')
			age=int(input('Enter the age of cricketer:\t'))
			country=input('Enter the country of cricketer:\t')
			record=(name,age,country)
			my_cursor.execute(sql_insert_query,record)
			my_con.commit()

		print(f'multiple records got inserted within :{database} database')

	except mysql.connector.Error as msg:
		print(f'The cause of the exception : {msg}')
	finally:
		close_connection(my_con,my_cursor)
if __name__ == '__main__':
	dynamic_insert_multiple_records()


