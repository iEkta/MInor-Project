from tkinter import * #imports everything from tkinter
import tkinter as tk  #aliasing tkinter as tk
from geopy.geocoders import Nominatim #Nominatim is a geocoder that uses OpenStreetMap data to find geographical coordinates 
from tkinter import ttk, messagebox #displaying message boxes.
from timezonefinder import TimezoneFinder #determine the timezone of a location given its latitude and longitude.
from datetime import datetime #to work with dates and times.
import requests # allows you to send HTTP requests to interact with web services and APIs.
import pytz #brings the Olson tz (timezone) database into Python
from PIL import Image, ImageTk #PIL is used for opening, manipulating, and saving many different image file formats

root=tk.Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Set the geometry to fullscreen
root.geometry(f"{screen_width}x{screen_height}+0+0")

# root = Tk() #This creates the main window of the application. Tk() initializes a tkinter application and returns the main window widget, which we assign to the variable root
root.title("Weather App") # sets the title of the main window to "Weather App"
# root.geometry("900x500+300+200") # sets the dimensions and position of the main window
# root.resizable(False, False) #disables the ability to resize the window

#Search box
Search_image = PhotoImage(file="Copy of search.png") #creates a PhotoImage object named Search_image by loading an image file named "Copy of search.png"
myimage = Label(image=Search_image)
myimage.place(x=20, y=20)

#text field
textfield= tk.Entry(root, justify="center", width=17, font=("poppins",25,"bold"),bg= "#404040", border=0, fg="white")
textfield.place(x=50,y=40)
textfield.focus()

#for opening the image
# img = Image.open("Copy of search.png")
# Display the image
# img.show()

Search_icon = PhotoImage(file="Copy of search_icon.png")
myimage_icon = Button(image=Search_icon, borderwidth=0, cursor="hand2",bg= "#404040")
myimage_icon.place(x=400,y=34)

#logo
Logo_image = PhotoImage(file= "Copy of logo.png")
logo = Label(image=Logo_image)
logo.place(x=150, y=100)

#Bottom box
Frame_image =PhotoImage(file="Copy of box.png")
frame_myimage = Label(image=Frame_image)
frame_myimage.pack(padx=5, pady=5,side= BOTTOM)

#label
label1= Label(root, text="WIND", font=("Helvetica", 15, 'bold'), fg="white", bg="#1ab5ef")
label1.place(x=120,y=400)

label2= Label(root, text="HUMIDITY", font=("Helvetica", 15, 'bold'), fg="white", bg="#1ab5ef")
label2.place(x=225,y=400)

label3= Label(root, text="DESCRIPTION", font=("Helvetica", 15, 'bold'), fg="white", bg="#1ab5ef")
label3.place(x=430,y=400)

label4= Label(root, text="PRESSURE", font=("Helvetica", 15, 'bold'), fg="white", bg="#1ab5ef")
label4.place(x=650,y=400)

t= Label(font=("arial",70,"bold"),fg= "#ee666d")
t.place(x=400, y=150)
c= Label(font=("arial",15, "bold"))
c.place(x=400, y=250)

w= Label(text="...", font=("arial",20, "bold"),bg="#1ab5ef")
w.place(x=120, y=430)
h= Label(text="...", font=("arial",20, "bold"),bg="#1ab5ef")
h.place(x=280, y=430)
d= Label(text="...", font=("arial",20, "bold"),bg="#1ab5ef")
d.place(x=450, y=430)
p= Label(text="...", font=("arial",20, "bold"),bg="#1ab5ef")
p.place(x=670, y=430)

root.mainloop()