#!/usr/bin/env python3


from tkinter import *
# from turtle import color, width
from PIL import Image, ImageTk
from datetime import *
import time
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
# Connecting to mysql database
import mysql.connector
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
        

mydb = mysql.connector.connect(host="localhost",
							user="root",
							password="arthur0204455@",
							database="richieblurDB")
mycursor = mydb.cursor()



my_window = Tk()
my_window = my_window
my_window.title("Hostel Search App")
my_window.geometry("1366x760")
my_window.resizable(0,0)
       #self.my_window.state()

       
bodyFrame1 = Frame(my_window,bg="#ffffff")
bodyFrame1.place(x=320,y=110,width=600,height=570)
            
  # Fecthing Data From mysql to my python progame
mycursor.execute("select HNAME, PRICE, LOCATION from hostel")
result = mycursor.fetchall

itemName = []
itemLocation = []
itemPrice = []

for i in mycursor:
        itemName.append(i[0])
        itemPrice.append(i[1])
        itemLocation.append(i[2])
        
	
print("Name of Students = ", itemName)
print("Marks of Students = ", itemPrice)
print("Marks of Students = ", itemLocation)

       #BODY FRAME ONE
        # create a figure
figure = Figure(figsize=(6, 4), dpi=100)

        # create FigureCanvasTkAgg object
figure_canvas = FigureCanvasTkAgg(figure, bodyFrame1)

        # create the toolbar
NavigationToolbar2Tk(figure_canvas, bodyFrame1)

        # create axes
axes = figure.add_subplot()

        # create the barchart
axes.bar(itemName, itemPrice,width=0.2)
axes.set_title('Hostel')
axes.set_ylabel('Popularity')

figure_canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

#******************
bodyFrame2 = Frame(my_window,bg="#ffffff")
bodyFrame2.place(x=910,y=110,width=450,height=570)
       # create a figure
figure = Figure(figsize=(6, 4), dpi=100)

        # create FigureCanvasTkAgg object
figure_canvas = FigureCanvasTkAgg(figure, bodyFrame2)

        # create the toolbar
NavigationToolbar2Tk(figure_canvas, bodyFrame2)

        # create axes
axes = figure.add_subplot()

        # create the barchart
axes.bar(itemLocation, itemPrice,width=0.2,color="cyan")
axes.set_title('Location')
axes.set_ylabel('Popularity')

figure_canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

#*************************
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
                             cursor="hand2",activebackground="#30D5C8", command=logout)
logout_text.place(x = 950,y = 15)
# logout_text = Button(header,text="Next",bg="#32cf8e",font=("",13,"bold"),bd=0,fg="white",
#                              cursor="hand2",activebackground="#32ef8e", command="
# logout_text.place(x = 920,y = 10)
        
    #****************************************************
                   #SIDEBAR
    #**************************************************** 

sidebar = Frame(my_window,bg="#ffffff")
sidebar.place(x = 0,y = 0,width = 300, height = 750)
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
dashboard_text = Button(sidebar,text = "Dashboard",bg="#ffffff",font=("",13,"bold"),bd=0,cursor="hand2",activebackground="#ffffff",command="")
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

search_text = Button(sidebar, text="Search", bg='#ffffff', font=("", 13, "bold"), bd=0,
                                    cursor='hand2', activebackground='#ffffff',command=searchHostel)
search_text.place(x=80, y=402)

        
        
        
        
     #****************************************************
                   #BODY
    #**************************************************** 

heading = Label(my_window,text="DashBoard",font=("",13,"bold"),fg="#0064d3",bg="#eff5f6")
heading.place(x=325,y = 75)   
 
        #BODY FRAME TWO
        
    
       
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
