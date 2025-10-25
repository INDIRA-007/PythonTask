import tkinter as tk
from tkinter import messagebox
import EmployeeDB as db

def open_emp_app():
    login_window.destroy()

    emp_window = tk.Tk()
    emp_window.title("Employee System Management")
    emp_window.geometry("500x400")

    name_var = tk.StringVar()
    age_var = tk.StringVar()
    dept_var = tk.StringVar()
    salary_var = tk.StringVar()

    # tk.Label(emp_window, text="Employee details Entry").pack(pady=10)
    # form_frame = tk.Frame(emp_window)
    # form_frame.pack(pady=10)

    tk.Label(emp_window, text="Name").grid(row=0,column=0,padx=5,pady=5)
    tk.Entry(emp_window, textvariable=name_var).grid(row=0,column=1)

    tk.Label(emp_window, text="Age").grid(row=1,column=0,padx=5,pady=5)
    tk.Entry(emp_window, textvariable=age_var).grid(row=1,column=1)

    tk.Label(emp_window, text="Department").grid(row=2,column=0,padx=5,pady=5)
    tk.Entry(emp_window, textvariable=dept_var).grid(row=2,column=1)

    tk.Label(emp_window, text="Salary").grid(row=3,column=0,padx=5,pady=5)
    tk.Entry(emp_window, textvariable=salary_var).grid(row=3,column=1)

    tk.Button(emp_window, text="Add Employee",command=db.insertEmployee).grid(row=4, column=0, pady=10)
    tk.Button(emp_window, text="View Employee").grid(row=4, column=1, pady=10)
    tk.Button(emp_window, text="Exit", command=emp_window.destroy).grid(row=5, column=0, pady=10)

    result_label = tk.Label(emp_window, text="Employee Records")
    result_label.grid(row=6,column=0,pady=10)


    name = name_var.get()
    age = age_var.get()
    dept = dept_var.get()
    salary = salary_var.get()

    emp_window.mainloop()

def validate_login():
    username = user_var.get()
    password = pass_var.get()

    if username == "admin" and password == "1234":
        messagebox.showinfo("Login successfully!","Welcome !! ")
        open_emp_app()
    elif username == "admin" and password == "1234":
        messagebox.showinfo("Login successfully!","Welcome !! ")
        # open_emp_app()
    else:
        messagebox.showerror("Login Failed","Invalide username of password")

db.createTable()


#Create Login Page
login_window = tk.Tk()
login_window.title("Login Page")
login_window.geometry("500x500")

user_var = tk.StringVar()
pass_var = tk.StringVar()

lable = tk.Label(login_window,text="Login",padx=10).pack(pady=10)

tk.Label(login_window,text="User Name: ").pack(pady=5)
tk.Entry(login_window,textvariable=user_var).pack()

tk.Label(login_window,text="Password:").pack(pady=5)
tk.Entry(login_window,textvariable=pass_var, show="*").pack()

tk.Button(login_window,text="Login", command=validate_login).pack(pady=15)

tk.Button(login_window,text="Exit",command=login_window.destroy).pack(pady=15)

login_window.mainloop()