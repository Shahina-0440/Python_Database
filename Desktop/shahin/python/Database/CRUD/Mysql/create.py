import mysql.connector
connection=mysql.connector.connect(host="localhost",user="root",password="Baba@2121",database="CRUDmysqlDatabase")
cursor=connection.cursor()

sql_st='''
create table user(uid int,uname varchar(32),uloc varchar(32))
'''
cursor.execute(sql_st)
connection.commit()
connection.close()
cursor.close()