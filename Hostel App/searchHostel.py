#!/usr/bin/env python3

import mysql.connector
from tkinter import *
from tkinter.ttk import Combobox, Treeview
from tkinter.ttk import Style
from turtle import bgcolor, right
from PIL import Image, ImageTk
from datetime import *
import time
from tkinter import messagebox

def hostelRegister():
    my_window.destroy()
    import hostelRegister   
        
def searchHostel():
    my_window.destroy()
    import searchHostel   
def dashboardHostel():
    my_window.destroy()
    import dashboard  
    
def logout():
    my_window.destroy()
    import loginRegister
        


#connection for phpmyadmin
def connection():
    conn = mysql.connector.connect(
        host='localhost',
        user='root', 
        password='arthur0204455@',
        db='richieblurDB',
    )
    return conn

def refreshTable():
    for data in text_output.get_children():
        text_output.delete(data)

    for array in read():
        text_output.insert(parent='', index='end', iid=array, text="", values=(array), tag="orow")

    text_output.tag_configure('orow', background='#EEEEEE', font=('Arial', 12))
    # text_output.grid(row=8, column=0, columnspan=5, rowspan=11, padx=10, pady=20)
    text_output.place(relheight=1,relwidth=1)


my_window = Tk()
my_window = my_window
my_window.title("Hostel Search App")
my_window.geometry("1366x760")
my_window.resizable(0,0)
       #self.my_window.state()
                
#************
#placeholders for entry
ph1 = StringVar()
ph2 = StringVar()
ph3 = StringVar()
ph4 = StringVar()
ph5 = StringVar()
ph6 = StringVar()
ph7 = StringVar()
ph8 = StringVar()

#placeholder set value function
def setph(word,num):
    if num ==1:
        ph1.set(word)
    if num ==2:
        ph2.set(word)
    if num ==3:
        ph3.set(word)
    if num ==4:
        ph4.set(word)
    if num ==5:
        ph5.set(word)
    if num ==6:
        ph6.set(word)
    if num ==7:
        ph7.set(word)
    if num ==8:
        ph7.set(word)
    
    

def read():
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM hostel")
    results = cursor.fetchall()
    conn.commit()
    conn.close()
    return results


def hostelSearch():
    itemName = str(hostelNameEntry.get())
    itemLocation = str(hostelLocationEntry.get())
    itemPrice = str(hostelPriceEntry.get())
    itemRoom = str(hostelRoomCombo.get())
   
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM hostel WHERE  HNAME='"+
    itemName+"' or LOCATION='"+
    itemLocation+"' or PRICE='"+
    itemPrice+"' or ROOM='"+
    itemRoom+"' ")
    
    
    try:
        result = cursor.fetchall()

        for num in range(0,8):
            setph(result[0][num],(num+1))

        conn.commit()
        conn.close()
    except:
        messagebox.showinfo("Error", "No data found")     
      
        #BODY FRAME TWO
       
bodyFrame2 = LabelFrame(my_window,text="Output",bg="#eff5f6",font=("",12,"bold"))
bodyFrame2.place(x=320,y=310,width=1040,height=390)
        
text_output = Treeview(bodyFrame2)

my_window.configure(bg="#eff5f6")
#Window Icon
Icon = PhotoImage(file="images/manage-icon.png")
my_window.iconphoto(True,Icon)
        
    
    #****************************************************
                   #HEADER
    #****************************************************
    

header = Frame(my_window, bg="#009ef4")
header.place(x = 300,y = 0,width = 1070,height = 60)
logout_text = Button(header,text="Logout",bg="#30D5C8",font=("",13,"bold"),bd=0,fg="white",
                             cursor="hand2",activebackground="#30D5C8",command=logout)
logout_text.place(x = 950,y = 15)
        
    #****************************************************
                   #SIDEBAR
    #**************************************************** 

sidebar = Frame(my_window,bg="#ffffff")
sidebar.place(x = 0,y = 0,width = 300, height = 500)
        #LOGO
logoImage = Image.open("images/hostel1.png")
photo = ImageTk.PhotoImage(logoImage)
logo = Label(sidebar,image=photo,bg="#ffffff")
logo.image = photo
logo.place(x = 70,y = 80)
#BRANDNAME
# brandName = Label(sidebar,text="Blurvo", bg="#ffffff",font=("",15,"bold"))
# brandName.place(x=80,y=200)
#**********
dashboardImage = Image.open("images/dashboard-icon.png")
photo = ImageTk.PhotoImage(dashboardImage)
dashboard = Label(sidebar,image=photo,bg="#ffffff")
dashboard.image = photo
dashboard.place(x=35, y =289)
#**********label
dashboard_text = Button(sidebar,text = "Dashboard",bg="#ffffff",font=("",13,"bold"),bd=0,cursor="hand2",activebackground="#ffffff",command=dashboardHostel)
dashboard_text.place(x=80, y=289)
#**********
         # Manage
manageImage = Image.open("images/manage-icon.png")
photo = ImageTk.PhotoImage(manageImage)
manage = Label(sidebar, image=photo, bg='#ffffff')
manage.image = photo
manage.place(x=35, y=340)
        

manage_text = Button(sidebar, text="Manage", bg='#ffffff', font=("", 13, "bold"), bd=0,
                                  cursor='hand2', activebackground='#ffffff',command=hostelRegister)
manage_text.place(x=80, y=345)

        # Settings
searchImage = Image.open("images/search4.png")
photo = ImageTk.PhotoImage(searchImage)
search = Label(sidebar, image=photo, bg='#ffffff')
search.image = photo
search.place(x=35, y=402)

settings_text = Button(sidebar, text="Search", bg='#ffffff', font=("", 13, "bold"), bd=0,
                                    cursor='hand2', activebackground='#ffffff',command=searchHostel)
settings_text.place(x=80, y=402)

     #****************************************************
                   #BODY
    #****************************************************         
heading = Label(my_window,text="Search",font=("",13,"bold"),fg="#0064d3",bg="#eff5f6")
heading.place(x=325,y = 75)   
        #BODY FRAME ONE
bodyFrame1 = Frame(my_window,bg="#ffffff")
bodyFrame1.place(x=320,y=110,width=1100,height=190)
        
        #************
hostelName = Label(bodyFrame1,text="Name",font=("",12),bg="#eff5f6",fg="#0064d3",relief="flat")
hostelName.place(x = 25, y=35)
hostelLocation = Label(bodyFrame1,text="Location",font=("",12),bg="#eff5f6",fg="#0064d3",relief="flat")
hostelLocation.place(x = 25, y=75)
hostelPrice = Label(bodyFrame1,text="Price",font=("",12),bg="#eff5f6",fg="#0064d3",relief="flat")
hostelPrice.place(x = 25, y=115)
hostelRoom = Label(bodyFrame1,text="Room",font=("",12),bg="#eff5f6",fg="#0064d3",relief="flat")
hostelRoom.place(x = 25, y=159)
        #**********
hostelNameEntry = Entry(bodyFrame1,width=50,bd=5,font=("", 12))
hostelNameEntry.config(highlightcolor="white",relief="sunken")
hostelNameEntry.place(x=225, y = 35)
hostelLocationEntry = Entry(bodyFrame1,width=50,bd=5,font=("", 12))
hostelLocationEntry.config(highlightcolor="white",relief="sunken")
hostelLocationEntry.place(x=225, y = 75)
hostelPriceEntry = Entry(bodyFrame1,width=50,bd=5,font=("", 12))
hostelPriceEntry.config(highlightcolor="white",relief="sunken")
hostelPriceEntry.place(x=225, y = 115)
hostelRoomCombo = Combobox(bodyFrame1,values =["Single","Double"],width=50)
hostelRoomCombo.place(x = 225, y=159)
        #***********
dashboard_text = Button(bodyFrame1,text = "Search",bg="#ffffff",font=("",13,"bold"),bd=0,cursor="hand2",activebackground="#ffffff",command=hostelSearch)
dashboard_text.place(x=800, y=150)
        
        

text_output.place(relheight=1,relwidth=1)

        #************
style = Style()
style.configure("Treeview.Heading", font=('Arial bold', 15))
text_output['columns'] = ("ID", "Name", "OwnerName","Location","Tel" ,"Price","Quantity","Room")
text_output.column("#0", width=0, stretch=NO)
text_output.column("ID", anchor=W, width=50)
text_output.column("Name", anchor=W, width=150)
text_output.column("OwnerName", anchor=W, width=150)
text_output.column("Location", anchor=W, width=150)
text_output.column("Tel", anchor=W, width=150)
text_output.column("Price", anchor=W, width=150)
text_output.column("Quantity", anchor=W, width=150)
text_output.column("Room", anchor=W, width=150)

text_output.heading("ID", text="ID", anchor=W)
text_output.heading("Name", text="Name", anchor=W)
text_output.heading("OwnerName", text="OwnerName", anchor=W)
text_output.heading("Location", text="Location", anchor=W)
text_output.heading("Tel", text="Tel", anchor=W)
text_output.heading("Price", text="Price", anchor=W)
text_output.heading("Quantity", text="Quantity", anchor=W)
text_output.heading("Room", text="Room", anchor=W)
        
    
refreshTable() 
       
   

        
        
#if __name__=="__name__":   


my_window.mainloop()
