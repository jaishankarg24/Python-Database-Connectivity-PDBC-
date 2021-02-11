import mysql.connector

host='localhost'
port=3306
user='root'
password='root123'
database='database_name'

def helper_function():
	data=input('sak OK to commit the changes:\t')
	if data.lower()=='ok':
		return True
	else:
		return False

def display_details(my_con,department):
	try:
		sql_select_query="""select * from `cricketer` where `department`=%s"""
		my_cursor=my_con.cursor()
		print('cursor object got created which is pointing to table ')
		input_data=(department,)
		my_cursor.execute(sql_select_query,input_data)
		records=my_cursor.fetchall()
		for record in records:
			print(f'Id: {record[0]}')
			print(f'Name: {record[1]}')
			print(f'Department: {record[2]}')
			print(f'Salary: {record[3]}')
	except mysql.connector.Error as msg:
		print(f'The cause of the exception : {msg}')
	finally:
		if my_con.is_connected():
			my_cursor.close()
			print('cursor object is closed')

def transactions():
	try:
		
		my_con=mysql.connector.connect(host=host,port=port,user=user,password=password,database=database)
		print(f'Python program got connected to the database: {database}')

		my_cursor=my_con.cursor()
		print('cursor object got created which is pointing to table ')

		print('Details before transactions')
		display_details(my_con,department='batting')
		print('******************************************************')
		print()
		display_details(my_con, department='allrounder')
		print('******************************************************')
		print()

		sql_delete_query="""delete from `cricketer` where `department`='allrounder' """
		sql_update_query="""update `cricketer` set `salary`=75000 where `department`='batting' """

		my_cursor.execute(sql_delete_query)
		my_cursor.execute(sql_update_query)

		ok=helper_function()
		if ok:
			my_con.commit()
		else:
			my_con.rollback()

		print('Details After transactions')
		print('******************************************************')
		display_details(my_con,department='batting')
		print('******************************************************')
		print()
		display_details(my_con, department='allrounder')
		print('******************************************************')
		print()

	except mysql.connector.Error as msg:
		print(f'The cause of the exception : {msg}')
	finally:
		if my_con.is_connected():
			my_con.close()
			print(f'connection got closed from the database: {database}')

if __name__ == '__main__':
	transactions()

