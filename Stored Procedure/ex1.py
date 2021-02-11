
'''Write a Python program to establish the connection with the database and count the no of cricketers present within the respective 
department using Stored Procedure'''

import mysql.connector

host='localhost'
port=3306
user='root'
password='root123'
database='database_name'

def close_connection(my_con,my_cursor):
	if my_con.is_connected():
		my_cursor.close()
		print('cursor object is closed')
		my_con.close()
		print(f'connection got closed from the database: {database}')


def count_the_cricketer():
	try:
		
		my_con=mysql.connector.connect(host=host,port=port,user=user,password=password,database=database)
		print(f'Python program got connected to the database: {database}')

		my_cursor=my_con.cursor()
		print('cursor object got created which is pointing to table ')

		procname='count_of_department'
		department=input('Enter the department name:\t')
		count=0
		procdata=(department,count)
		records=my_cursor.callproc(procname,procdata)
		print(records)		
		print(f'The number of criketer present in the department:{records[0]} :{records[1]}')

	except mysql.connector.Error as msg:
		print(f'The cause of the exception : {msg}')
	finally:
		close_connection(my_con,my_cursor)

if __name__ == '__main__':
	count_the_cricketer()
