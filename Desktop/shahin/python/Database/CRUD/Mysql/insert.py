import mysql.connector
connection=mysql.connector.connect(host="localhost",user="root",password="Baba@2121",database="CRUDmysqlDatabase")
cursor=connection.cursor()

#data=(1,"shahin","bangalore")
data=[(2,"chote","hyd"),(3,"gundu","hyd")]
sql_st='''
insert into user(uid,uname,uloc) values (%s,%s,%s)
'''
#cursor.execute(sql_st,data)
cursor.executemany(sql_st,data)
connection.commit()


connection.close()
cursor.close()