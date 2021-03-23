import mysql.connector
import tkinter,os
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "mismet1985",
    database = "the_warehouse"
)

mycursor = mydb.cursor()


root = Tk()

img = ImageTk.PhotoImage(Image.open("truck.png"))
panel = Label(root, image = img)
panel.pack(side = "bottom", fill = "both", expand = "yes")

root.tk.call('wm', 'iconphoto', root._w, tkinter.PhotoImage(file='truck.png'))
root.geometry("600x400")
root.title('CHANGE PRODUCT INFO')

Title_label = Label(root, text = '======== Change product info in database ========', font = "35")
Title_label.grid (row=0,column=0, columnspan = 4)

product_id = Label(root, text = "Enter product id: ")
product_id.grid(row=1,column=0)

global product_id_e
product_id_e = Entry(root, width=40)
product_id_e.grid(row=1,column=1)

Product_name = Label(root, text = "Enter new product name: ")
Product_name.grid(row=2,column=0)

global product_name_e
product_name_e = Entry(root, width=40)
product_name_e.grid(row=2,column=1)

Product_type = Label(root, text = "Enter new product type id: ")
Product_type.grid(row=3,column=0)

global Product_type_e
Product_type_e = Entry(root, width=40)
Product_type_e.grid(row=3,column=1)

Product_code = Label(root, text = "Enter new product code: ")
Product_code.grid(row=4,column=0)

global Product_code_e
Product_code_e = Entry(root, width=40)
Product_code_e.grid(row=4,column=1)

Product_quantity = Label(root, text = "Enter new product quantity: ")
Product_quantity.grid(row=5,column=0)

global Product_quantity_e
Product_quantity_e = Entry(root, width=40)
Product_quantity_e.grid(row=5,column=1)

Product_supplier = Label(root, text = "Enter new product supplier id: ")
Product_supplier.grid(row=6,column=0)

global Product_supplier_e
Product_supplier_e = Entry(root, width=40)
Product_supplier_e.grid(row=6,column=1)

Product_price = Label(root, text = "Enter new product price: ")
Product_price.grid(row=7,column=0)

global Product_price_e
Product_price_e = Entry(root, width=40)
Product_price_e.grid(row=7,column=1)

empty_label = Label(root, text = '  ')
empty_label.grid (row=8,column=0)

empty_label2 = Label(root, text = '  ')
empty_label2.grid (row=10,column=0)


def product_update():
    product_to_c = product_id_e.get()
    name = product_name_e.get()
    p_type = Product_type_e.get()
    code = Product_code_e.get()
    quantity = Product_quantity_e.get()
    supplier = Product_supplier_e.get()
    price = Product_price_e.get()
    
    sql_update_product = "UPDATE products SET product_name = %s, idproduct_type = %s ,product_code = %s ,product_quantity = %s ,idsupplier = %s,product_price = %s WHERE idproducts = %s"
    values = (name,p_type,code,quantity,supplier,price,product_to_c)
    mycursor.execute(sql_update_product, values)
    mydb.commit()
    
    if employeeChange:
        change_p_s()
        root.destroy()
    

def change_p_s():
    messagebox.showinfo("Submit", "New product info successfully changed")

def supplier_list():
    os.system('supplier_list.py')

def product_type_list():
    os.system('product_type_list.py')

def exit_main():
    
    root.destroy()

employeeChange = tkinter.Button(root, text = "Save changed product info",padx=45,command=product_update, pady=10, fg="blue", bg="white")
listSuppliers = tkinter.Button(root, text = "List suppliers",padx=18,command=supplier_list, pady=5, fg="blue", bg="white")
listProductType = tkinter.Button(root, text = "List product types",padx=5,command=product_type_list, pady=5, fg="blue", bg="white")
exitButton = tkinter.Button(root,text = "EXIT", padx=80, pady=20, command=exit_main, fg="black", bg="red")


employeeChange.grid(row=9,column=1)
listSuppliers.grid(row=6 , column = 3)
listProductType.grid(row=3 , column = 3)
exitButton.grid(row=11, column=1, columnspan=2)



root.mainloop()
