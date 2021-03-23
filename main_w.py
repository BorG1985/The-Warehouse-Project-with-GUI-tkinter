# import mysql.connector,os,time
import tkinter,os
#from employees_menu import Tk as e_menu
from tkinter import *
from tkinter import messagebox

root = Tk()
root.tk.call('wm', 'iconphoto', root._w, tkinter.PhotoImage(file='truck.png'))
root.geometry("365x400")
root.title('Welcome to Warehouse main window')

Employees_label = Label(root, text = "For employees click on button : ")
Employees_label.grid(row=2,column=0)

Product_label = Label(root, text = "For products click on button : ")
Product_label.grid(row=3,column=0)

Product_label = Label(root, text = "For suppliers click on button : ")
Product_label.grid(row=4,column=0)

empty_label = Label(root, text = '  ')
empty_label.grid (row=5,column=0)


def employees():
    os.system('employees_menu.py')

def products():
    os.system('product_menu.py')

def suppliers():
    os.system('suppliers_menu.py')


def main_manu():         
    #e_menu()
    return


def exit_main():
    
    root.destroy()

    
appSubject = Label(root, text = "Welcome to THE WAREHOUSE database system!", font = "40")
employeesButton = tkinter.Button(root, text = "Employees",padx=45,command=employees, pady=10, fg="blue", bg="white")
productsButton = tkinter.Button(root, text = "Products",padx=50,command=products, pady=10, fg="blue", bg="white")
suppliersButton = tkinter.Button(root, text = "Suppliers",padx=49,command=suppliers, pady=10, fg="blue", bg="white")
exitButton = tkinter.Button(root,text = "EXIT", padx=80, pady=20, command=exit_main, fg="black", bg="red")


appSubject.grid(row=0,column=0, columnspan=2)
employeesButton.grid(row=2,column=1)
productsButton.grid(row=3,column=1)
suppliersButton.grid(row=4,column=1)
exitButton.grid(row=6, column=0, columnspan=2)



root.mainloop()
