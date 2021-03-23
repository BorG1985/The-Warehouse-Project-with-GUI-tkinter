import os
import tkinter
from tkinter import *

root = Tk()
root.tk.call('wm', 'iconphoto', root._w, tkinter.PhotoImage(file='truck.png'))
root.geometry("300x400")
root.title('EMPLOYEE MENU')

empty_label = Label(root, text = '  ')
empty_label.grid (row=6,column=0)


def new_e():
    os.system('new_employee.py')

def change_e():
    os.system('change_employee_info.py')

def erase_e():
    os.system('erase_employee.py')

def list_e():
    os.system('employees_list.py')


def exit_main():
    
    root.destroy()

    
appSubject = Label(root, text = "THE WAREHOUSE database system!\nEMPLOYEES MENU", font = "40")
NewEmployeesButton = tkinter.Button(root, text = "New Employee",command=new_e,padx=82, pady=10, fg="blue", bg="white")
ChangeEmployeeButton = tkinter.Button(root, text = "Change Employee info",command=change_e,padx=61, pady=10, fg="blue", bg="white")
EraseEmployeeButton = tkinter.Button(root, text = "Erase Employee",command=erase_e, pady=10,padx=80, fg="blue", bg="white")
ListAllEmployeesButton = tkinter.Button(root, text = "List all employees",command=list_e,padx=75, pady=10, fg="blue", bg="white")
exitButton = tkinter.Button(root,text = "EXIT",padx=110, pady=10, command=exit_main, fg="black", bg="red")


appSubject.grid(row=0,column=1, columnspan=3)
NewEmployeesButton.grid(row=2,column=1, columnspan=3)
ChangeEmployeeButton.grid(row=3,column=1, columnspan=3)
EraseEmployeeButton.grid(row=4,column=1, columnspan=3)
ListAllEmployeesButton.grid(row=5,column=1, columnspan=3)
exitButton.grid(row=6, column=1, columnspan=3)

root.mainloop()