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
root.title('NEW SUPPLIER')

Supplier_name = Label(root, text = "Enter supplier name: ")
Supplier_name.grid(row=2,column=0)

global Supplier_name_e
Supplier_name_e = Entry(root, width=50)
Supplier_name_e.grid(row=2,column=1)

Supplier_location = Label(root, text = "Enter supplier location: ")
Supplier_location.grid(row=3,column=0)

global Supplier_location_e
Supplier_location_e = Entry(root, width=50)
Supplier_location_e.grid(row=3,column=1)

Supplier_address = Label(root, text = "Enter supplier address: ")
Supplier_address.grid(row=4,column=0)

global Supplier_address_e
Supplier_address_e = Entry(root, width=50)
Supplier_address_e.grid(row=4,column=1)


empty_label = Label(root, text = '  ')
empty_label.grid (row=5,column=0)

empty_label = Label(root, text = '  ')
empty_label.grid (row=7,column=0)


def supplier_insert():
    name = Supplier_name_e.get()
    location = Supplier_location_e.get()
    address = Supplier_address_e.get()
    
    sql_enter_supplier = "INSERT INTO supplier (supplier_name,supplier_location,supplier_address) VALUES (%s,%s,%s)"
    values = (name,location,address)
    mycursor.execute(sql_enter_supplier, values)
    mydb.commit()
    
    if employeeInsert:
        new_s_s()
        root.destroy()
    

def new_s_s():
    messagebox.showinfo("Submit", "New supplier successfully added")

def exit_main():
    
    root.destroy()

employeeInsert = tkinter.Button(root, text = "Save new supplier info",padx=45,command=supplier_insert, pady=10, fg="blue", bg="white")
exitButton = tkinter.Button(root,text = "EXIT", padx=80, pady=20, command=exit_main, fg="black", bg="red")


employeeInsert.grid(row=6,column=1)
exitButton.grid(row=8, column=1, columnspan=2)



root.mainloop()
