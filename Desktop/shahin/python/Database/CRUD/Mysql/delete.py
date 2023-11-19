import mysql.connector
connection=mysql.connector.connect(host="localhost",user="root",password="Baba@2121",database="CRUDmysqlDatabase")
cursor=connection.cursor()


user_id_to_delete=1
sql_st='''
delete from user where uid=%s
'''
cursor.execute(sql_st,(user_id_to_delete,))
connection.commit()


connection.close()
cursor.close()