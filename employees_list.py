import mysql.connector
import tkinter,os
from tkinter import *
from tkinter import messagebox
from tkinter import ttk 

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "mismet1985",
    database = "the_warehouse"
)

mycursor = mydb.cursor()


root = Tk()
root.tk.call('wm', 'iconphoto', root._w, tkinter.PhotoImage(file='truck.png'))
root.geometry("275x400")
root.title('Employees List')



empty_label = Label(root, text = '  ')
empty_label.grid (row=15,column=0)


sql = "SELECT idemployees, employee_name, employee_last_name, employee_address, employee_sector FROM employees"
mycursor.execute(sql)
employees = mycursor.fetchall()
for ind,i in enumerate(employees):
    names_label = Label(root)
    names_label.grid(row=int(ind)+1, column=0)
    names_label.config(text=i)

separator = ttk.Separator(root,orient="horizontal")
separator.place(relx=0, rely=0.67, relwidth=1, relheight=1) 

def exit_main():
    
    root.destroy()

exitButton = tkinter.Button(root,text = "EXIT", padx=80, pady=20, command=exit_main, fg="black", bg="red")

exitButton.grid(row=17, column=0, columnspan=2)



root.mainloop()
