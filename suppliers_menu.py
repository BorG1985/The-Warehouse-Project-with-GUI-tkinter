import os,time
import tkinter
from tkinter import *

root = Tk()
root.tk.call('wm', 'iconphoto', root._w, tkinter.PhotoImage(file='truck.png'))
root.geometry("275x400")
root.title('SUPPLIERS MENU')


empty_label = Label(root, text = '  ')
empty_label.grid (row=6,column=0)


def new_s():
    os.system('new_supplier.py')

def change_s():
    os.system('change_supplier_info.py')

def erase_s():
    os.system('erase_supplier.py')

def list_s():
    os.system('supplier_list.py')


def exit_main():
    
    root.destroy()

    
appSubject = Label(root, text = "THE WAREHOUSE database system!\nPRODUCT MENU", font = "40")
NewProductButton = tkinter.Button(root, text = "New Supplier",command=new_s, padx=79, pady=10, fg="blue", bg="white")
ChangeProductButton = tkinter.Button(root, text = "Change Supplier info",command=change_s,padx=59, pady=10, fg="blue", bg="white")
EraseProductButton = tkinter.Button(root, text = "Erase Supplier",command=erase_s,padx=78, pady=10, fg="blue", bg="white")
ListAllProductsButton = tkinter.Button(root, text = "List all Suppliers",command=list_s,padx=72, pady=10, fg="blue", bg="white")
exitButton = tkinter.Button(root,text = "EXIT",padx=103, pady=20, command=exit_main, fg="black", bg="red")


appSubject.grid(row=0,column=0, columnspan=3)
NewProductButton.grid(row=2,column=0, columnspan=3)
ChangeProductButton.grid(row=3,column=0, columnspan=3)
EraseProductButton.grid(row=4,column=0, columnspan=3)
ListAllProductsButton.grid(row=5,column=0, columnspan=3)
exitButton.grid(row=6, column=0, columnspan=3)

root.mainloop()