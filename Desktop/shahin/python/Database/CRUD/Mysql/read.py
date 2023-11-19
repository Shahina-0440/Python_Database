import mysql.connector
connection=mysql.connector.connect(host="localhost",user="root",password="Baba@2121",database="CRUDmysqlDatabase")
cursor=connection.cursor()
"""sql_st='''
select * from user
'''
"""

sql_st='''
select uid from user
'''
cursor.execute(sql_st)
result=cursor.fetchall()
for i in result:
    print(i)


cursor.close()
connection.close()
