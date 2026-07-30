import mysql.connector

mydb = None
cursor = None
try:
    mydb = mysql.connector.connect(
        host="localhost",      # MySQL server name
        user="root",
        password="jit@12345",
        database="db1"
    )

    if mydb.is_connected():
        print("Connected to MySQL database")
        cursor = mydb.cursor()
    else:
        print("Not connected to MySQL database")

except mysql.connector.Error as e:
    print("error connecting MySQL", e)
finally:
    if cursor is not None:
        cursor.close()
    if mydb is not None and mydb.is_connected():
        mydb.close()
