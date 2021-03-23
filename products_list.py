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
root.geometry("275x400")
root.title('Products List')



empty_label = Label(root, text = '  ')
empty_label.grid (row=15,column=0)


sql = "SELECT * FROM products"
mycursor.execute(sql)
products = mycursor.fetchall()
for ind,i in enumerate(products):
    names_label = Label(root)
    names_label.grid(row=int(ind)+1, column=0)
    names_label.config(text=i)

def exit_main():
    
    root.destroy()

exitButton = tkinter.Button(root,text = "EXIT", padx=80, pady=20, command=exit_main, fg="black", bg="red")

exitButton.grid(row=16, column=0, columnspan=2)



root.mainloop()
