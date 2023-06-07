from tkinter import *
import tkinter as tk 
from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox
from timezonefinder import timezonefinder
from datetime import datetime
import requests
import pytz 

root=Tk()
root.title("weather App")
root.geometry("800x400+200+100")
root.resizable(False,false)

def getWeather():
  try 
    city=text_field.get()
    geolocator=Nominatim(user_agent="geoapiExercises")
    location=geolocator.geocode(city)
    obj=TimezoneFinder()
    result=obj.timezone_at(lng=location.longitude,lat=location.latitude)
    print(result)

    home=pytz.timezone(result)
    local_time=datetime.now(home)
    current_time=local_time.strftimr("%I:%M %p")
    clock.config(text=current_time)
    name.config(text="CURRENT WEATHER")
    