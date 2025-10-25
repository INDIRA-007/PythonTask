import  mysql.connector
from mysql.connector import Error

# function to create a database connection
def dbConnection():
    """ create a database connection to the MySQL database """
    return mysql.connector.connect(
        host = "127.0.0.1",
        user = "root",
        password = "admin",
        database = "emp_db_python",
        port=3306
    )

#function to create table
def createTable():
    try:
        conn = dbConnection()
        cursor = conn.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS Employees(
        Id INT Auto_Increment Primary Key ,
        Name VARCHAR(50), 
        Age INT, 
        Department VARCHAR(50), 
        Salary FLOAT)""")
        print("Employees table created successfully.")
    
    except Error as e:
        print(f"Error creating table: {e}")
    
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

# function to insert employee data
def insertEmployee():
    try:
        conn = dbConnection()
        cursor = conn.cursor()
        name = input("Enter Employee Name: ")
        age = int(input("Enter Employee Age: "))
        department = input("Enter Employee Department: ")
        salary = float(input("Enter Employee Salary: "))

        insert_query = """INSERT INTO Employees (Name, Age, Department, Salary) 
                        VALUES (%s, %s, %s, %s)"""
        data = (name, age, department, salary)
        cursor.execute(insert_query, data)
        print("Employee data inserted successfully.")
        conn.commit()
    except Error as e:
        print("Error on inserting data:", e)
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()
#function to view all employees
def viewEmployee():
    try:
        conn = dbConnection()
        cursor = conn.cursor()
        cursor.execute("Select * from Employees")
        rows = cursor.fetchall()
        print("Employee Details\n")
        for row in rows:
            print(f"Id: {row[0]}, Name: {row[1]}, Age: {row[2]}, Department: {row[3]}, Salary: {row[4]}")

    except Error as e:
        print("Error on viewing employee details",e)
    finally:
        cursor.close()
        conn.close()

#function to update employee details
def updateEmployee():
    try:
        conn = dbConnection()
        cursor = conn.cursor()
        Emp_id = int(input("Enter the EmployeeId to update value: "))
        new_salary = float(input("Enter the new salary: "))
        new_salary_confirm = float(input("Enter the new salary: "))

        if new_salary == new_salary_confirm:
            cursor.execute("Update Employees SET salary value = %s where Id= %s",(new_salary,Emp_id))
            conn.commit()
        else:
            print("Enter the salary and confirm salary not matched!")
    except Error as e:
        print("Error in update: ", e)
    finally:
        cursor.close()
        conn.close()

#function to delete employee
def deleteEmployee():
    try:
        conn = dbConnection()
        cursor = conn.cursor()
        Emp_id = int(input("Enter the EmployeeId to delete: "))
        cursor.execute("DELETE FROM Employees where id %s",(Emp_id,))
        conn.commit()
    except Error as e:
        print("Error to delete data: ",e)
    finally:
        cursor.close()
        conn.close()

#main menu
def main_menu():
    #Check DB has the table
    createTable()

    while True:
        print("\n***Employee Management System***")
        print("1. Add Employee")
        print("2. View Employee")
        print("3. Update Employee salary")
        print("4. Delete Employee data")
        print("5. Exit")

        choice = int(input("Enter your choice (1-5): "))
        if choice == 1:
            insertEmployee()
        elif choice == 2:
            viewEmployee()
        elif choice == 3:
            updateEmployee()
        elif choice == 4:
            deleteEmployee()
        elif choice == 5:
            print("Exiting application...")
            break
        else:
            print("Invalid choice. Please try again...")

main_menu()
# if __name__ == "main":
#     main_menu()