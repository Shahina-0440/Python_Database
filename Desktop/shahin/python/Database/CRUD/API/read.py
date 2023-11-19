import mysql.connector
try:
    db=mysql.connector.connect(host="localhost",user="root",password="Baba@2121",database="api_user")
    cur=db.cursor()
    sql_st='''
    select * from users
    '''
    cur.execute(sql_st)
    d=cur.fetchall()
    for i in d:
        print(i)
except mysql.connector.DatabaseError as err:
    print(err)
finally:
    if db:
        db.close()
    if cur:
        cur.close()
