import tkinter as tk
import requests
import time

def getWeather(canvas):
    city = textfiled.get()
    api = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=79c5660a520b22caf39f6de6e3ae5306"
    json_data = requests.get(api).json()
    print(json_data)
    condition = json_data['weather'][0]['main']
    temp = int(json_data['main']['temp'] - 273.15)
    min_temp = int(json_data['main']['temp_min'] - 273.15)
    max_temp = int(json_data['main']['temp_max'] - 273.15)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']
    sunrise = time.strftime("%I:%M:%S", time.gmtime(json_data['sys']['sunrise']-21600))
    sunset = time.strftime("%I:%M:%S", time.gmtime(json_data['sys']['sunset']-21600))

    final_info = condition + "\n" + str(temp) + "degree C"
    final_data = "\n" + "Max Temp : "+str(max_temp)+"\n"+"Min Temp : "+str(min_temp)+"\n Pressure"+str(pressure)+"\n Humidity"+str(humidity)+"\n"+"Wind speed-"+str(wind)+"\nSunrise-"+str(sunrise)+"\nSunset"+str(sunset)
    label1.config(text = final_info)
    label2.config(text = final_data)



canvas = tk.Tk()
canvas.geometry("600x500")
canvas.title("Weather App")

f = ("poppins",15,"bold")
t = ("poppins",35,"bold")

textfiled = tk.Entry(canvas, font = t)
textfiled.pack(pady = 20)
textfiled.focus()
textfiled.bind('<Return>', getWeather)

label1 = tk.Label(canvas, font = t)
label1.pack()
label2 = tk.Label(canvas, font = f)
label2.pack()

canvas.mainloop()