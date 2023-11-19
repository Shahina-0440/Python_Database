import mysql.connector
connection=mysql.connector.connect(host="localhost",user="root",password="Baba@2121",database="CRUDmysqlDatabase")
cursor=connection.cursor()

user_loc="chennai"
user_id_to_update=1
sql_st='''
update user set uloc=%s where uid=%s
'''
cursor.execute(sql_st,(user_loc,user_id_to_update))
connection.commit()


connection.close()
cursor.close()