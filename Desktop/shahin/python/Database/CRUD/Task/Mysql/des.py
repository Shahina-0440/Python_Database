import mysql.connector

db = mysql.connector.connect(host="localhost", user="root", password="Baba@2121", database="api_products")
cur = db.cursor()
cur.execute('''
    SELECT * FROM products
    ORDER BY pid DESC
''')

result = cur.fetchall()
for product in result:
    print(product)

cur.close()
db.close()