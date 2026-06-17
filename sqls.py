import mysql.connector
from mysql.connector import Error
try:
    connection=mysql.connector.connect(
        host='localhost',
        user='root',
        database='test',
        password='root'
    )

    if connection.is_connected():
        print("Connected successfully")

        cursor=connection.cursor()
        cursor.execute("Select * from customer")
        rows=cursor.fetchall()

        for row in rows:
            print(row)

except Error as e:
    print("Exception",e)
finally:
        if connection.is_connected():
            connection.close()
