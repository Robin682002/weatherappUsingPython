from tkinter import *
from tkinter import ttk
from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

root = Tk()
root.title("weather app")
root.geometry("900x500+300+200")
root.resizable(False, False)



def getWeather():
    city = textfield.get()

      # Get city name from text field entry

    

    try:
        

        # Geocoding and time zone handling
        geolocator = Nominatim(user_agent="geoapiExercises")
        location = geolocator.geocode(city)
        
        
        obj = TimezoneFinder()
        result = obj.timezone_at(lng=location.longitude, lat=location.latitude)
        print(result)


        home = pytz.timezone(result)
        local_time = datetime.now(home)
        current_time = local_time.strftime("%I:%M %p")

        # Update time and weather labels
        clock.config(text=current_time)
        name.config(text="CURRENT WEATHER - " + city.title())

        # Weather API call
        api = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=57baf9c40fc7d5fbbc03b84b420aa60a"
        json_data = requests.get(api).json()

        # Get temperature, condition, description, wind speed, humidity

        condition = json_data['weather'][0]['main']
        description = json_data['weather'][0]['description']
        temp = int(json_data['main']['temp'] - 273.15)
        pressure = json_data['main']['pressure']
        humidity = json_data['main']['humidity']
        wind = json_data['wind']['speed']

        t.config(text=(temp, "°"))
        c.config(text=(condition, "|", "FEELS LIKE", temp, "°"))
        w.config(text=(wind, "Km/h"))
        h.config(text=(humidity, "%"))
        p.config(text=(pressure, "hPa"))

    except Exception as e:
        messagebox.showerror("Weather App","Invalid Entry")



       


search_image = PhotoImage(file="pythonProject\Copy of search.png")  
myimage_label = Label(image=search_image)
myimage_label.place(x=20, y=20)

textfield = ttk.Entry(root, justify="center", width=17, font=("poppins", 25, "bold"),  background="#404040", foreground="black")
                      


textfield.place(x = 50, y = 40)

textfield.focus()




search_icon = PhotoImage(file="pythonProject\Copy of search_icon.png")
myimage_icon = Button(image=search_icon, borderwidth=0, cursor="hand2", background = "#404040", command=getWeather) 
myimage_icon.place(x=400, y=34)


logo_image = PhotoImage(file="pythonProject\Copy of logo.png")
logo_image_label = Label(image=logo_image)
logo_image_label.place(x=150, y=130)


Frame_image = PhotoImage(file="pythonProject\Copy of box.png")
Frame_image_label = Label(image=Frame_image)
Frame_image_label.pack(padx=5, pady=5, side=BOTTOM)


name = Label(root,  font=("arial", 15, "bold"))
name.place(x=30, y=100)
clock = Label(root, font=("Helvetica", 20,  "bold") )
clock.place(x=30, y=130)



Label1 = Label(root,text = "WIND", font=("arial", 20, "bold"),
                  background="#1ab5ef", foreground="white"
)

Label1.place(x=120, y=397)

Label2 = Label(root,text = "HUMIDITY", font=("arial", 20, "bold"),
                  background="#1ab5ef", foreground="white"
)

Label2.place(x=220, y=397)


Label3 = Label(root,text = "DESCRIPTION", font=("arial", 20, "bold"),
                  background="#1ab5ef", foreground="white"
)

Label3.place(x=430, y=397)



Label4 = Label(root,text = "PRESSURE", font=("arial", 20, "bold"),
                  background="#1ab5ef", foreground="white"
)

Label4.place(x=650, y=397)


t=Label(font=("arial", 70, "bold"), fg = "#ffa500")
t.place(x=400, y=150)
c = Label(font=("arial", 20, "bold"))
c.place(x=400, y=250)

w=Label(text="...",font=("arial", 20, "bold"),bg="#1ab5ef")
w.place(x=140, y=430)

h = Label(text="...",font=("arial", 20, "bold"),bg="#1ab5ef")
h.place(x=240, y=430)

d = Label(text="...",font=("arial", 20, "bold"),bg="#1ab5ef")
d.place(x=450, y=430)

p = Label(text="...",font=("arial", 20, "bold"),bg="#1ab5ef")
p.place(x=650, y=430)












root.mainloop()






