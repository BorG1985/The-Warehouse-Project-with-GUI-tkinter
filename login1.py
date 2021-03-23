import mysql.connector,os,time
import tkinter
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
root.geometry("400x200")
root.title('Login to The Warehouse')

Username_label = Label(root, text = "Username: ")
Username_label.grid(row=2,column=0)

Password_label = Label(root, text = "Password: ")
Password_label.grid(row=3,column=0)

global username_e
username_e = Entry(root, width=40)
username_e.grid(row=2,column=1)

global password_e
password_e = Entry(root, width=40)
password_e.grid(row=3,column=1)



def login_f():
    
    
    username = username_e.get()
    password = password_e.get()

    sql_authentication = "SELECT * FROM employees WHERE employee_username = %s AND employee_password = %s"
    values = (username, password)
    mycursor.execute(sql_authentication,values)

    account = mycursor.fetchall()

    for i in account:
        employee_name = i[1]
        employee_last_name = i[2]
        employee_username = i[6]
        employee_password = i[7]
        idpermisions = i[5]
    
    if username == employee_username and password == employee_password:
        print("You are now logged in as",employee_name, employee_last_name)
        print("Welcome ",employee_name, employee_last_name)
       
        login_s()
        root.destroy()
        
        
        return username, password


def login_s():
    messagebox.showinfo("Succeess", "Successful login!")

    
appSubject = Label(root, text = "Welcome to THE WAREHOUSE database system!", font = "40")
myLabel2 = Label(root, text = "This is login form", font="20")
myButton = tkinter.Button(root, text = "Submit",padx=50,command=login_f, pady=10, fg="blue", bg="white")


appSubject.grid(row=0,column=0, columnspan=2)
myLabel2.grid(row=1,column=0)
myButton.grid(row=4,column=1)



root.mainloop()
