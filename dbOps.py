import mysql.connector
from mysql.connector import Error

# Error = mysql.connector.Error
try:
    db = mysql.connector.connect(
        host = "127.0.0.1",
        user ="root",
        password="admin",
        database="emp_db_python",
        port=3306
    )
    cur = db.cursor()
    #cur.execute("CREATE DATABASE IF NOT EXISTS emp_db_python")
    
    #--- 1.To write data into the database table ----
    
    #cur.execute("CREATE TABLE IF NOT EXISTS Employees(Id INT Primary key, Name Varchar(50), Age INT, Mobile INT)")    
    #query = "CREATE TABLE IF NOT EXISTS Employees(Id INT Primary key, Name Varchar(50), Age INT, Mobile INT)"
    # insert_query="INSERT INTO Employees(Id, Name, Age, Mobile) VALUES(%s,%s,%s,%s)"
    # data = [(1,'John Doe',30,12345),(2,'Jane Smith',25,98765),(3,'Alice Johnson',28,55566)]
    # cur.executemany(insert_query,data)

    # db.commit()
    # print(cur.rowcount, "Records inserted successfully into Employees table")

    #---- 2.To read data from the database table ----
    
    # cur.execute("SELECT * FROM Employees")
    # rows = cur.fetchall()
    # print(type(rows))

    # print("data from Employees table:")
    # for row in rows:
    #     print(row)

    #---- 3.To delete data from the database table ----

    # delete_query = "DELETE FROM Employees WHERE Id = %s"
    # id_to_delete = (3,)
    # cur.execute(delete_query, id_to_delete)
    # db.commit()
    # print(cur.rowcount, "Record deleted successfully from Employees table")

    #---- 4.To update data in the database table ----

    update_query = "UPDATE Employees SET Age = %s WHERE Id = %s"
    new_age = (35, 2)
    cur.execute(update_query, new_age)
    db.commit()
    print(cur.rowcount, "Record updated successfully in Employees table")

     #---- 5.To read data from the database table after update ---- 
    cur.execute("SELECT * FROM Employees")
    rows = cur.fetchall()
    print("data from Employees table after update:")
    for row in rows:
        print(row)


    cur.close()
    db.close()
    
except Error as e:
    print("Connection failed: ",e)
# if db.is_connected():
#     print(" Connection successful")

# creating database
# open the file -> connection the db
# edit the file -> modify the values
# close the file -> close the connection


