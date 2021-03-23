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
root.geometry("350x300")
root.title('Welcome to Warehouse main window')

empty_label = Label(root, text = '  ')
empty_label.grid (row=1,column=0)

Employee_id = Label(root, text = "Enter employee id: ")
Employee_id.grid(row=2,column=0)

global Employee_id_e
Employee_id_e = Entry(root, width=31)
Employee_id_e.grid(row=2,column=1)

empty_label = Label(root, text = '  ')
empty_label.grid (row=3,column=0)

empty_label = Label(root, text = '  ')
empty_label.grid (row=5,column=0)


def employee_eraser():
    employee_to_erase = Employee_id_e.get()
    
    sql_erase_employee = "DELETE FROM employees WHERE idemployees = %s"
    values = (employee_to_erase,)
    mycursor.execute(sql_erase_employee, values)
    mydb.commit()
    
    if employeeErase:
        erase_e_s()
        root.destroy()
    

def erase_e_s():
    messagebox.showinfo("Submit", "Employee successfully deleted")

def exit_main():
    
    root.destroy()

employeeErase = tkinter.Button(root, text = "Delete employee",padx=45,command=employee_eraser, pady=10, fg="blue", bg="white")
exitButton = tkinter.Button(root,text = "EXIT", padx=80, pady=20, command=exit_main, fg="black", bg="red")


employeeErase.grid(row=4,column=1, columnspan=2)
exitButton.grid(row=6, column=1, columnspan=2)



root.mainloop()
