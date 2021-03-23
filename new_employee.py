import mysql.connector
import tkinter,os
from tkinter import *
from tkinter import messagebox

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "mismet1985",
    database = "the_warehouse"
)

mycursor = mydb.cursor()


root = Tk()
root.tk.call('wm', 'iconphoto', root._w, tkinter.PhotoImage(file='truck.png'))
root.geometry("500x300")
root.title('Welcome to Warehouse main window')

Employee_name = Label(root, text = "Enter employee name: ")
Employee_name.grid(row=2,column=0)

global Employee_name_e
Employee_name_e = Entry(root, width=50)
Employee_name_e.grid(row=2,column=1)

Employee_last_name = Label(root, text = "Enter employee last name: ")
Employee_last_name.grid(row=3,column=0)

global Employee_last_name_e
Employee_last_name_e = Entry(root, width=50)
Employee_last_name_e.grid(row=3,column=1)

Employee_address = Label(root, text = "Enter employee address: ")
Employee_address.grid(row=4,column=0)

global Employee_address_e
Employee_address_e = Entry(root, width=50)
Employee_address_e.grid(row=4,column=1)

Employee_sector = Label(root, text = "Enter employee sector: ")
Employee_sector.grid(row=5,column=0)

global Employee_sector_e
Employee_sector_e = Entry(root, width=50)
Employee_sector_e.grid(row=5,column=1)

Employee_permision = Label(root, text = "Enter employee permision: ")
Employee_permision.grid(row=6,column=0)

global Employee_permision_e
Employee_permision_e = Entry(root, width=50)
Employee_permision_e.grid(row=6,column=1)

Employee_username = Label(root, text = "Enter employee username: ")
Employee_username.grid(row=7,column=0)

global Employee_username_e
Employee_username_e = Entry(root, width=50)
Employee_username_e.grid(row=7,column=1)

Employee_password = Label(root, text = "Enter employee password: ")
Employee_password.grid(row=8,column=0)

global Employee_password_e
Employee_password_e = Entry(root, width=50)
Employee_password_e.grid(row=8,column=1)

empty_label = Label(root, text = '  ')
empty_label.grid (row=11,column=0)


def employee_insert():
    name = Employee_name_e.get()
    last_name = Employee_last_name_e.get()
    address = Employee_address_e.get()
    sector = Employee_sector_e.get()
    permisions = Employee_permision_e.get()
    username = Employee_username_e.get()
    password = Employee_password_e.get()
    
    sql_enter_employee = "INSERT INTO employees (employee_name,employee_last_name,employee_address,employee_sector,idpermisions,employee_username,employee_password) VALUES (%s,%s,%s,%s,%s,%s,%s)"
    values = (name,last_name,address,sector,permisions,username,password)
    mycursor.execute(sql_enter_employee, values)
    mydb.commit()
    
    # if employee_insert():
    #     new_e_s()
    #     root.destroy()
    if employeeInsert:
        new_e_s()
        root.destroy()
    

def new_e_s():
    messagebox.showinfo("Submit", "New employee successfully added")

def exit_main():
    
    root.destroy()

employeeInsert = tkinter.Button(root, text = "Save new employee info",padx=45,command=employee_insert, pady=10, fg="blue", bg="white")
exitButton = tkinter.Button(root,text = "EXIT", padx=80, pady=20, command=exit_main, fg="black", bg="red")


employeeInsert.grid(row=10,column=1)
exitButton.grid(row=12, column=0, columnspan=2)



root.mainloop()
