import mysql.connector

connection = mysql.connector.connect(host='localhost', port='3306', database='flaskData', user='root', password='CSGO123abcDf.')
cursor = connection.cursor()

cursor.execute('SELECT username, password FROM users')
users = cursor.fetchall()

for user in users:
    print(f"Username: {user[0]}, Password: {user[1]}")

cursor.close()
connection.close()
