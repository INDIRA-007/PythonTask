#pyQT
#tkinter
#turtle
import tkinter as tk

def say_greet():
    print("Welcome!")

def greet_user():
    name = entry.get()
    lbl_result.config(text=f"Hello, {name}!!!")



root = tk.Tk()
root.title("My Page")
root.geometry("300x500")


lbl = tk.Label(root,text="Hello",font=("Arial",20),background="#9b3bc4",padx=10,pady=15)
# lbl.pack()
#lbl.place(x=100,y=100)
lbl.grid(row=0, column=0)

entry = tk.Entry(root)
entry.grid(row=0,column=1, pady=10)

button = tk.Button(root, text="Exit",padx=10,pady=5, command=greet_user)
#button.place(x=200,y=250)
button.grid(row=1,column=0)

lbl_result = tk.Label(root,text="")
lbl_result.grid(row=1,column=1)

button = tk.Button(root, text="Greet",padx=10,pady=5, command=say_greet)
#button.place(x=150,y=200)
button.grid(row=0,column=0)

choice = ""
tk.Radiobutton(root,text="Python",variable=choice)


# tk.Entry

root.mainloop()