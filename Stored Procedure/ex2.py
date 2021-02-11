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


def fetch_the_data():
	try:
		
		my_con=mysql.connector.connect(host=host,port=port,user=user,password=password,database=database)
		print(f'Python program got connected to the database: {database}')

		my_cursor=my_con.cursor()
		print('cursor object got created which is pointing to table ')

		procname='display_data'
		department=input('Enter the department name:\t')
		procdata=(department,)
		records=my_cursor.callproc(procname,procdata)
		print(records)

		my_complete_record=my_cursor.stored_results()	
		print(my_complete_record)	

		for i in my_complete_record:
			print(i.fetchall())
		

	except mysql.connector.Error as msg:
		print(f'The cause of the exception : {msg}')
	finally:
		close_connection(my_con,my_cursor)

if __name__ == '__main__':
	fetch_the_data()

