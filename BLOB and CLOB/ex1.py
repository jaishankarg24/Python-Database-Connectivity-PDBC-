#BLOB

import mysql.connector

host='localhost'
port=3306
user='root'
password='root123'
database='naukridatbase'

#Converting the data into binary format
def convert_to_binary(filepath):
	with open(file=filepath,mode='rb') as f:
		binary=f.read()
	return binary

def close_connection(my_con,my_cursor):
	if my_con.is_connected():
			my_cursor.close()
			print('cursor object is closed')
			my_con.close()
			print(f'connection got closed from the database: {database}')

def insert_records():
	try:
		
		my_con=mysql.connector.connect(host=host,port=port,user=user,password=password,database=database)
		print(f'Python program got connected to the database: {database}')

		my_cursor=my_con.cursor()
		print('cursor object got created which is pointing to table ')

		#insert into tablename(column names) values(%s)
		sql_insert_query="""insert into `jobtable` (`name`,`address`,`resume`,`photo`,`video`) values(%s,%s,%s,%s,%s) """

		name=input('Enter the name of the candidate:\t')
		address=input('Enter the address of the candidate:\t')

		resume_location='F:\\filepath\\resume.pdf'
		photo_location='F:\\filepath\\image.jpeg'
		video_location='F:\\filepath\\vid.mp4'

		resume=convert_to_binary(resume_location)
		photo=convert_to_binary(photo_location)
		video=convert_to_binary(video_location)
		
		input_data=(name,address,resume,photo,video)
		my_cursor.execute(sql_insert_query,input_data)

		my_con.commit()
		print(f'Data got inserted into the table: jobtable present within the database:{database}')

	except mysql.connector.Error as msg:
		print(f'The cause of the exception : {msg}')
	finally:
		close_connection(my_con,my_cursor)

if __name__ == '__main__':
	insert_records()
