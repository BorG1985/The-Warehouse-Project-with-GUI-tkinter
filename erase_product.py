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

Product_id = Label(root, text = "Enter product id: ")
Product_id.grid(row=2,column=0)

global Product_id_e
Product_id_e = Entry(root, width=31)
Product_id_e.grid(row=2,column=1)

empty_label = Label(root, text = '  ')
empty_label.grid (row=3,column=0)

empty_label = Label(root, text = '  ')
empty_label.grid (row=5,column=0)


def product_eraser():
    product_to_erase = Product_id_e.get()
    
    sql_erase_employee = "DELETE FROM products WHERE idproducts = %s"
    values = (product_to_erase,)
    mycursor.execute(sql_erase_employee, values)
    mydb.commit()
    
    if employeeErase:
        erase_e_s()
        root.destroy()
    

def erase_e_s():
    messagebox.showinfo("Submit", "Product successfully deleted")

def exit_main():
    
    root.destroy()

employeeErase = tkinter.Button(root, text = "Delete product",padx=45,command=product_eraser, pady=10, fg="blue", bg="white")
exitButton = tkinter.Button(root,text = "EXIT", padx=80, pady=20, command=exit_main, fg="black", bg="red")


employeeErase.grid(row=4,column=1, columnspan=2)
exitButton.grid(row=6, column=1, columnspan=2)



root.mainloop()
