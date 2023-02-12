#!/usr/bin/env python3
from tkinter import *
from tkinter import messagebox
import mysql.connector

def next():
    import hostelRegister

def login():
    conn = mysql.connector.connect(
        host='localhost',
        user='root', 
        password='arthur0204455@',
        db='richieblurDB'
    )
    
    cursor = conn.cursor()

    # find_user = f'SELECT Email,Password FROM User_db WHERE Email = {str(user.get())} and Password = {str(code.get())}'
    cursor.execute("SELECT Email,Password FROM  User_db WHERE  Email='"+
    str(user.get())+"' and Password='"+
    str(code.get())+"'")

    result = cursor.fetchall()
    if result:
        messagebox.showinfo("Success", 'Logged in Successfully.')
        root.destroy()
        next()
    else:
        messagebox.showerror("Failed", "Wrong Login details, please try again.")



root = Tk()
root.title('Login')
root.geometry("925x500+300+200")
root.configure(bg="#eff5f6")
root.resizable(False,False)
        #Window Icon
Icon = PhotoImage(file="images/logo.png")
root.iconphoto(True,Icon)
        

img = PhotoImage(file="images/search.png")
Label(root,image=img,bg="white").place(x=20,y=50)

frame =Frame(root,width=385,height=320,bg='white')
frame.place(x=520,y = 70)

heading = Label(frame,text="Sign In",fg="#57a1f8",bg="white",font=('Miicrosoft YaHei UI Light',23,'bold'))
heading.place(x=100,y=5)
#*********************************************
def on_enter(e):
    user.delete(0,"end")
    
def on_leave(e):
    name = user.get()
    if name == "":
        user.insert(0,'Username')
        
user= Entry(frame,width=30,fg='black',border=0,bg='white',font=('Miicrosoft YaHei UI Light',11))
user.place(x=30,y=80,height=30)
user.insert(0,'Username')
user.bind('<FocusIn>',on_enter)
user.bind('<FocusOut>',on_leave)

Frame(frame,width=295,height=2,bg="black").place(x=25,y=107)

#******************************************
def on_enter(e):
    code.delete(0,"end")
    
def on_leave(e):
    name = code.get()
    if name == "":
        code.insert(0,'Password')
        
code= Entry(frame,width=30,fg='black',border=0,bg='white',font=('Miicrosoft YaHei UI Light',11))
code.place(x=30,y=150,height=30)
code.insert(0,'Password')
code.bind('<FocusIn>',on_enter)
code.bind('<FocusOut>',on_leave)
Frame(frame,width=295,height=2,bg="black").place(x=25,y=177)
#**************************************************
Button(frame,width=39,pady=7,text="Sign in",bg="#57a1f8",fg='white',border=0, command=login).place(x=26,y=204)
def password_command2():
    if code.cget('show') == '•':
        code.config(show='')
    else:
        code.config(show='•')


checkButton = Checkbutton(frame ,bg='#f8f8f8', command=password_command2, text='Hide')
checkButton.place(x=320, y=150)


# ============ LOGIN DATABASE CONNECTION =========
# connection  = mysql.connector.connect(
#         host='localhost',
#         user='root', 
#         password='arthur0204455@',
#         db='richieblurDB',
#     )
# cur = connection.cursor()
# cur.execute("CREATE TABLE IF NOT EXISTS RegLog(Email TEXT PRIMARY KEY, FullName TEXT, Password TEXT, "
#             "ConfirmPassword TEXT)")
# connection.commit()
# connection.close()



root.mainloop()
