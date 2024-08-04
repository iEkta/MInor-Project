from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz
from PIL import Image, ImageTk

root=tk.Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Set the geometry to fullscreen
root.geometry(f"{screen_width}x{screen_height}+0+0")
# root = Tk()
root.title("Weather App")
# root.geometry("900x500+300+200")
# root.resizable(False, False)

def getWeather():
    try:
        city = textfield.get()
    
        geolocator = Nominatim(user_agent="geoapiExercises")
        location = geolocator.geocode(city)
        obj = TimezoneFinder()
        result = obj.timezone_at(lng=location.longitude, lat= location.latitude)
    
        home= pytz.timezone(result)
        local_time = datetime.now(home)
        current_time= local_time.strftime("%I:%M %p")
        clock.config(text=current_time)
        name.config(text="CURRENT WEATHER")
    
        #weather
        api= "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=f8b24ccb89f7825675944fce01208375"
    
        json_data = requests.get(api).json()
        condition = json_data['weather'][0]['main']
        description = json_data['weather'][0]['description']
        temp  = int(json_data['main']['temp']-273.15)
        pressure = json_data['main']['pressure']
        humidity = json_data['main']['humidity']
        wind = json_data['wind']['speed']
    
        t.config(text=(temp,"°"))
        c.config(text=(condition,"|","FEELS","LIKE",temp,"°"))
    
        w.config(text=wind)
        h.config(text=humidity)
        d.config(text=description)
        p.config(text=pressure)
        # print(result)
        
    except Exception as e:
        messagebox.showerror("Weather App", "Invalid Entry!!")
        
#Search box
Search_image = PhotoImage(file="Copy of search.png")
myimage = Label(image=Search_image)
myimage.place(x=120, y=100)

#text field
textfield= tk.Entry(root, justify="center", width=17, font=("poppins",25,"bold"),bg= "#404040", border=0, fg="white")
textfield.place(x=150,y=120)
textfield.focus()

#for opening the image
# img = Image.open("Copy of search.png")
# Display the image
# img.show()

Search_icon = PhotoImage(file="Copy of search_icon.png")
myimage_icon = Button(image=Search_icon, borderwidth=0, cursor="hand2",bg= "#404040", command=getWeather)
myimage_icon.place(x=500, y=114)

#logo
Logo_image = PhotoImage(file= "Copy of logo.png")
logo = Label(image=Logo_image)
logo.place(x=350, y=260)

#Bottom box
Frame_image =PhotoImage(file="Copy of box.png")
frame_myimage = Label(image=Frame_image)
frame_myimage.place(x=350,y=600)

#time
name= Label(root,font=('arial',22,"bold"))
name.place(x=100, y=250)
clock = Label(root,font=("Helvetica",27))
clock.place(x=100,y=330)

#label
label1= Label(root, text="WIND", font=("Helvetica", 20, 'bold'), fg="white", bg="#1ab5ef")
label1.place(x=400,y=630)

label2= Label(root, text="HUMIDITY", font=("Helvetica", 20, 'bold'), fg="white", bg="#1ab5ef")
label2.place(x=550,y=630)

label3= Label(root, text="DESCRIPTION", font=("Helvetica", 20, 'bold'), fg="white", bg="#1ab5ef")
label3.place(x=700,y=630)

label4= Label(root, text="PRESSURE", font=("Helvetica", 20, 'bold'), fg="white", bg="#1ab5ef")
label4.place(x=930,y=630)

t= Label(font=("arial",80,"bold"),fg= "#ee666d")
t.place(x=700, y=250)
c= Label(font=("arial",25, "bold"))
c.place(x=700, y=400)

w= Label(text="...", font=("arial",20, "bold"),bg="#1ab5ef")
w.place(x=400, y=660)
h= Label(text="...", font=("arial",20, "bold"),bg="#1ab5ef")
h.place(x=550, y=660)
d= Label(text="...", font=("arial",20, "bold"),bg="#1ab5ef")
d.place(x=700, y=660)
p= Label(text="...", font=("arial",20, "bold"),bg="#1ab5ef")
p.place(x=930, y=660)

root.mainloop()