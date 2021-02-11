import mysql.connector
if __name__ == '__main__':
	try:

		host='localhost'
		port=3306
		user='root'
		password='root123'
		database='onlinebatch'
		
		my_connection=mysql.connector.connect(host=host,port=port,user=user,
															password=password,database=database)
		print(f'Python program got connected to the database: {database}')

	except mysql.connector.Error as msg:
		print(f'The cause of the exception : {msg}')
	finally:
		my_connection.close()
		print(f'connection got closed with : {database} database')

# o/p:
# ----
# Python program got connected to the database: onlinebatch
# connection got closed with : onlinebatch database