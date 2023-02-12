#!/usr/bin/env python3



import mysql.connector
from tkinter import *
from tkinter.ttk import Combobox, Treeview
from tkinter.ttk import Style
from PIL import Image, ImageTk
from datetime import *
import time

from tkinter import messagebox
#from execute import *

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
my_window.title("Hostel Search App")
my_window.geometry("1366x760")
my_window.resizable(0,0)

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

def add():
    itemCode = str(hostelNameID.get())
    itemName = str(hostelNameEntry.get())
    ownerName = str(hostelOwnerNameEntry.get())
    itemLocation = str(hostelLocationEntry.get())
    itemTel = str(hostelTelEntry.get())
    itemPrice = str(hostelPriceEntry.get())
    itemQuantity = str(hostelQuantityEntry.get())
    itemRoom = str(hostelRoomCombo.get())

    if (itemCode == "" or itemCode == " ") or(itemName == "" or itemName == " ") or (ownerName == "" or ownerName == " ") or (itemLocation == "" or itemLocation == " ") or (itemTel == "" or itemTel == " ") or (itemPrice == "" or itemPrice == " ")or (itemQuantity == "" or itemQuantity == " ")or (itemRoom == "" or itemRoom == " "):
        messagebox.showinfo("Error", "Please fill up the blank entry")
        return
    else:
        try:
            query = (f"INSERT INTO `hostel` (`HTLID`, `HNAME`, `ONAME`, `LOCATION`, `TEL`,`PRICE`,`QUANTITY`,`ROOM`) VALUES('{itemCode}', '{itemName}', '{ownerName}', '{itemLocation}', '{itemTel}', '{itemPrice}','{itemQuantity}','{itemRoom}')")
            conn = connection()
            cursor = conn.cursor()
            cursor.execute(query)
            conn.commit()
            conn.close()
        except:
            messagebox.showinfo("Error", "Htl ID already exist")
            print(cursor)
            return

    refreshTable()

def reset():
    decision = messagebox.askquestion("Warning!!", "Delete all data?")
    if decision != "yes":
        return 
    else:
        try:
            conn = connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM hostel")
            conn.commit()
            conn.close()
        except:
            messagebox.showinfo("Error", "Sorry an error occured")
            return

        refreshTable()
def delete():
    decision = messagebox.askquestion("Warning!!", "Delete the selected data?")
    if decision != "yes":
        return 
    else:
        selected_item = text_output.selection()[0]
        deleteData = str(text_output.item(selected_item)['values'][0])
        try:
            conn = connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM hostel WHERE HTLID='"+str(deleteData)+"'")
            conn.commit()
            conn.close()
        except:
            messagebox.showinfo("Error", "Sorry an error occured")
            return

        refreshTable()
def select():
    try:
        selected_item = text_output.selection()[0]
        itemCode = str(text_output.item(selected_item)['values'][0])
        itemName = str(text_output.item(selected_item)['values'][1])
        ownerName = str(text_output.item(selected_item)['values'][2])
        location = str(text_output.item(selected_item)['values'][3])
        tel = str(text_output.item(selected_item)['values'][4])
        Price = str(text_output.item(selected_item)['values'][5])
        Quantity = str(text_output.item(selected_item)['values'][6])
        room = str(text_output.item(selected_item)['values'][7])

        setph(itemCode,1)
        setph(itemName,2)
        setph(ownerName,3)
        setph(location,4)
        setph(tel,5)
        setph(Price,6)
        setph(Quantity,7)
        setph(room,8)
    except:
        messagebox.showinfo("Error", "Please select a data row") 

def update():
    selectedhtldid = ""

    try:
        selected_item = text_output.selection()[0]
        selectedhtldid = str(text_output.item(selected_item)['values'][0])
    except:
        messagebox.showinfo("Error", "Please select a data row")

    itemCode = str(hostelNameID.get())
    itemName = str(hostelNameEntry.get())
    ownerName = str(hostelOwnerNameEntry.get())
    itemLocation = str(hostelLocationEntry.get())
    itemTel = str(hostelTelEntry.get())
    itemPrice = str(hostelPriceEntry.get())
    itemQuantity = str(hostelQuantityEntry.get())
    itemRoom = str(hostelRoomCombo.get())


    if (itemCode == "" or itemCode == " ") or(itemName == "" or itemName == " ") or (ownerName == "" or ownerName == " ") or (itemLocation == "" or itemLocation == " ") or (itemTel == "" or itemTel == " ") or (itemPrice == "" or itemPrice == " ")or (itemQuantity == "" or itemQuantity == " ")or (itemRoom == "" or itemRoom == " "):
        messagebox.showinfo("Error", "Please fill up the blank entry")
        return
    else:
        try:
            conn = connection()
            cursor = conn.cursor()
            cursor.execute("UPDATE students SET HTLID='"+
            itemCode+"', HNAME='"+
            itemName+"', ONAME='"+
            ownerName+"', LOCATION='"+
            itemLocation+"', TEL='"+
            itemTel+"', PRICE='"+
            itemPrice+"', QUANTITY='"+
            itemQuantity+"', ROOM='"+
            itemRoom+"' WHERE HTLID='"+
            selectedhtldid+"' ")
            conn.commit()
            conn.close()
        except:
            messagebox.showinfo("Error", "Stud ID already exist")
            return
    refreshTable()
        #BODY FRAME TWO
bodyFrame2 = LabelFrame(my_window,text="Output",bg="#eff5f6",font=("",12,"bold"))
bodyFrame2.place(x=40,y=510,width=1300,height=190)
       #**************
text_output = Treeview(bodyFrame2)
     

      
       
    # def backgroundCreate(self):
my_window.configure(bg="#eff5f6")
        #Window Icon
Icon = PhotoImage(file="images/manage-icon.png")
my_window.iconphoto(True,Icon)
        
    
    #****************************************************
                   #HEADER
    #****************************************************
    
    # def headerCreate(self):
header = Frame(my_window, bg="#009ef4")
header.place(x = 300,y = 0,width = 1070,height = 60)
logout_text = Button(header,text="Logout",bg="#30D5C8",font=("",13,"bold"),bd=0,fg="white",
                             cursor="hand2",activebackground="#30D5C8",command=logout)
logout_text.place(x = 950,y = 15)
        
    #****************************************************
                   #SIDEBAR
    #**************************************************** 
    # def sidebarCreate(self):
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
                                  cursor='hand2', activebackground='#ffffff',command="")
manage_text.place(x=80, y=345)

        # Settings
searchImage = Image.open("images/search4.png")
photo = ImageTk.PhotoImage(searchImage)
search = Label(sidebar, image=photo, bg='#ffffff')
search.image = photo
search.place(x=35, y=402)

search_text = Button(sidebar, text="Search", bg='#ffffff', font=("", 13, "bold"), bd=0,
                                    cursor='hand2', activebackground='#ffffff',command=searchHostel)
search_text.place(x=80, y=402)

     #****************************************************
                   #BODY
    #**************************************************** 
    # def bodyCreate(self):
heading = Label(my_window,text="Manage",font=("",13,"bold"),fg="#0064d3",bg="#eff5f6")
heading.place(x=325,y = 75)   
        #BODY FRAME ONE
bodyFrame1 = Frame(my_window,bg="#ffffff")
bodyFrame1.place(x=320,y=110,width=1040,height=350)
        
        #INPUT LABELS
hostelName = Label(bodyFrame1,text="Name",font=("",12),bg="#eff5f6",fg="#0064d3",relief="flat")
hostelName.place(x = 25, y=35)

hostelCode = Label(bodyFrame1,text="Hostel Code",font=("",12),bg="#eff5f6",fg="#0064d3",relief="flat")
hostelCode.place(x = 775, y=40)
        
hostelOwnerName = Label(bodyFrame1,text="Owner Name",font=("",12),bg="#eff5f6",fg="#0064d3",relief="flat")
hostelOwnerName.place(x = 25, y=75)
        
hostelLocation = Label(bodyFrame1,text="Location",font=("",12),bg="#eff5f6",fg="#0064d3",relief="flat")
hostelLocation.place(x = 25, y=115)
        
hostelTel = Label(bodyFrame1,text="Tel",font=("",12),bg="#eff5f6",fg="#0064d3",relief="flat")
hostelTel.place(x = 25, y=155)
        
hostelPrice = Label(bodyFrame1,text="Price",font=("",12),bg="#eff5f6",fg="#0064d3",relief="flat")
hostelPrice.place(x = 25, y=195)
        
hostelQuantity = Label(bodyFrame1,text="Quantity",font=("",12),bg="#eff5f6",fg="#0064d3",relief="flat")
hostelQuantity.place(x = 25, y=235)
        
hostelRoom = Label(bodyFrame1,text="Room",font=("",12),bg="#eff5f6",fg="#0064d3",relief="flat")
hostelRoom.place(x = 25, y=275)
        #INPUT Entry
hostelQuantityEntry = Entry(bodyFrame1,width=50,bd=5,font=("", 12),textvariable=ph7)
hostelQuantityEntry.config(highlightcolor="white",relief="sunken")
hostelQuantityEntry.place(x = 225, y=235)
        
        
hostelPriceEntry = Entry(bodyFrame1, width=50,bd=5,font=("", 12),textvariable=ph6)
hostelPriceEntry.config(highlightcolor="white",relief="sunken")
hostelPriceEntry.place(x=225,y=195)
        
hostelTelEntry = Entry(bodyFrame1,width=50,bd=5,font=("", 12),textvariable=ph5)
hostelTelEntry.config(highlightcolor="white",relief="sunken")
hostelTelEntry.place(x=225,y=155)
        
        
hostelLocationEntry = Entry(bodyFrame1,width=50,bd=5,font=("", 12),textvariable=ph4)
hostelLocationEntry.config(highlightcolor="white",relief="sunken")
hostelLocationEntry.place(x=225, y =115)
        
        
hostelOwnerNameEntry= Entry(bodyFrame1,width=50,bd=5,font=("", 12),textvariable=ph3)
hostelOwnerNameEntry.config(highlightcolor="white",relief="sunken")
hostelOwnerNameEntry.place(x=225, y = 75)
        
        
hostelNameEntry = Entry(bodyFrame1,width=50,bd=5,font=("", 12),textvariable=ph2)
hostelNameEntry.config(highlightcolor="white",relief="sunken")
hostelNameEntry.place(x=225, y = 35)

hostelNameID = Entry(bodyFrame1,width=10,bd=5,font=("", 12),textvariable=ph1)
hostelNameID.config(highlightcolor="white",relief="sunken")
hostelNameID.place(x=890, y = 35)      
        
hostelRoomCombo = Combobox(bodyFrame1,values =["Single","Double"],width=50,textvariable=ph8)
hostelRoomCombo.place(x = 225, y=275)
    #****************
    

    

        #*******************
dashboard_done = Button(bodyFrame1,text = "Done",bg="#ffffff",font=("",13,"bold"),bd=0,cursor="hand2",activebackground="#ffffff",command=add)
dashboard_done.place(x=625, y=300)

dashboard_select = Button(bodyFrame1,text = "Select",bg="#ffffff",font=("",13,"bold"),bd=0,cursor="hand2",activebackground="#ffffff",command=select)
dashboard_select.place(x=530, y=300)

dashboard_reset = Button(bodyFrame1,text = "Reset",bg="#ffffff",font=("",13,"bold"),bd=0,cursor="hand2",activebackground="#ffffff",command=reset)
dashboard_reset.place(x=710, y=300)

dashboard_update = Button(bodyFrame1,text = "update",bg="#ffffff",font=("",13,"bold"),bd=0,cursor="hand2",activebackground="#ffffff",command=update)
dashboard_update.place(x=800, y=300)

dashboard_delete = Button(bodyFrame1,text = "Delete",bg="#ffffff",font=("",13,"bold"),bd=0,cursor="hand2",activebackground="#ffffff",command=delete)
dashboard_delete.place(x=900, y=300)

        

        

text_output.place(relheight=1,relwidth=1)
style = Style()
style.configure("Treeview.Heading", font=('Arial bold', 15))

text_output['columns'] = ("ID", "Name", "OwnerName","Location","Tel" ,"Price","Quantity","Room")
text_output.column("#0", width=0, stretch=NO)
text_output.column("ID", anchor=W, width=20)
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
       

        
def nextPage():
    my_window.destroy()
    import hostelRegister        
def nextPage1():
    my_window.destroy()
    import searchHostel   
def nextPage2():
    my_window.destroy()
    import dashboard  

my_window.mainloop()
