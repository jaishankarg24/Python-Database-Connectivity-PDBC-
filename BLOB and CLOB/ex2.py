#BLOB

import mysql.connector

host='localhost'
port=3306
user='root'
password='root123'
database='naukridatbase'

#Converting data from binary format to actual format
def convert_from_binary(filepath,filedata):
	with open(file=filepath,mode='wb') as f:
		f.write(filedata)
	
def close_connection(my_con,my_cursor):
	if my_con.is_connected():
			my_cursor.close()
			print('cursor object is closed')
			my_con.close()
			print(f'connection got closed from the database: {database}')

def select_records():
	try:
		
		my_con=mysql.connector.connect(host=host,port=port,user=user,password=password,database=database)
		print(f'Python program got connected to the database: {database}')

		my_cursor=my_con.cursor()
		print('cursor object got created which is pointing to table ')

		#select * from tablename where columnname
		sql_select_query="""select * from `jobtable` where `id`=%s """

		id=int(input('Enter the id of the candidate:\t'))
		
		input_data=(id,)
		my_cursor.execute(sql_select_query,input_data)
		records=my_cursor.fetchone()
		# print(records)
		print(f'ID: {records[0]}')
		print(f'Name: {records[1]}')
		print(f'Address: {records[2]}')

		binary_resume=records[3]
		binary_photo=records[4]
		binary_video=records[5]

		#path of the new files 
		resume_location='F:\\new filepath\\new_resume.pdf'
		photo_location='F:\\new filepath\\new_photo.jpeg'
		video_location='F:\\new filepath\\new_video.mp4'
		
		#converting the binary data to actual format 
		convert_from_binary(resume_location,binary_resume)
		convert_from_binary(photo_location,binary_photo)
		convert_from_binary(video_location,binary_video)

		print('data got fetched from the database....')

	except mysql.connector.Error as msg:
		print(f'The cause of the exception : {msg}')
	finally:
		close_connection(my_con,my_cursor)

if __name__ == '__main__':
	select_records()
