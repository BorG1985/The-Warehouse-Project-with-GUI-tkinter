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
root.geometry("550x400")
root.title('NEW PRODUCT')

Title_label = Label(root, text = '======== Enter new product in database ========', font = "35")
Title_label.grid (row=0,column=0, columnspan = 4)

empty_label1 = Label(root, text = '  ')
empty_label1.grid (row=1,column=0)

Product_name = Label(root, text = "Enter product name: ")
Product_name.grid(row=2,column=0)

global product_name_e
product_name_e = Entry(root, width=40)
product_name_e.grid(row=2,column=1)

Product_type = Label(root, text = "Enter product type id: ")
Product_type.grid(row=3,column=0)

global Product_type_e
Product_type_e = Entry(root, width=40)
Product_type_e.grid(row=3,column=1)

Product_code = Label(root, text = "Enter product code: ")
Product_code.grid(row=4,column=0)

global Product_code_e
Product_code_e = Entry(root, width=40)
Product_code_e.grid(row=4,column=1)

Product_quantity = Label(root, text = "Enter product quantity: ")
Product_quantity.grid(row=5,column=0)

global Product_quantity_e
Product_quantity_e = Entry(root, width=40)
Product_quantity_e.grid(row=5,column=1)

Product_supplier = Label(root, text = "Enter product supplier id: ")
Product_supplier.grid(row=6,column=0)

global Product_supplier_e
Product_supplier_e = Entry(root, width=40)
Product_supplier_e.grid(row=6,column=1)

Product_price = Label(root, text = "Enter product price: ")
Product_price.grid(row=7,column=0)

global Product_price_e
Product_price_e = Entry(root, width=40)
Product_price_e.grid(row=7,column=1)

empty_label = Label(root, text = '  ')
empty_label.grid (row=8,column=0)

empty_label2 = Label(root, text = '  ')
empty_label2.grid (row=10,column=0)


def product_insert():
    name = product_name_e.get()
    p_type = Product_type_e.get()
    code = Product_code_e.get()
    quantity = Product_quantity_e.get()
    supplier = Product_supplier_e.get()
    price = Product_price_e.get()
    
    sql_enter_product = "INSERT INTO products (product_name,idproduct_type,product_code,product_quantity,idsupplier,product_price) VALUES (%s,%s,%s,%s,%s,%s)"
    values = (name,p_type,code,quantity,supplier,price)
    mycursor.execute(sql_enter_product, values)
    mydb.commit()
    
    
    if productInsert:
        new_e_s()
        root.destroy()
    

def new_e_s():
    messagebox.showinfo("Submit", "New product successfully added")

def supplier_list():
    os.system('supplier_list.py')

def product_type_list():
    os.system('product_type_list.py')

def exit_main():
    
    root.destroy()

productInsert = tkinter.Button(root, text = "Save new product info",padx=45,command=product_insert, pady=10, fg="blue", bg="white")
listSuppliers = tkinter.Button(root, text = "List suppliers",padx=18,command=supplier_list, pady=5, fg="blue", bg="white")
listProductType = tkinter.Button(root, text = "List product types",padx=5,command=product_type_list, pady=5, fg="blue", bg="white")
exitButton = tkinter.Button(root,text = "EXIT", padx=80, pady=20, command=exit_main, fg="black", bg="red")


productInsert.grid(row=9,column=1)
listSuppliers.grid(row=6 , column = 3)
listProductType.grid(row=3 , column = 3)
exitButton.grid(row=11, column=1, columnspan=2)



root.mainloop()
