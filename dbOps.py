import mysql.connector
from mysql.connector import Error

# Error = mysql.connector.Error
try:
    db = mysql.connector.connect(
        host = "127.0.0.1",
        user ="root",
        password="admin",
        database="hr",
        port=3306
    )
except Error as e:
    print("Connection failed: ",e)


if db.is_connected():
    print(" Connection successful")