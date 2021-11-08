import tkinter as tk
import requests
import time

# Func to get Data from API
def getWeather(canvas):
    city = textfield.get()
    # API URl ---->   https://openweathermap.org/api
    api = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=06c921750b9a82d8f5d1294e1586276f"    # PATH / URL

    json_data = requests.get(api).json()    # To get the json data
    condition = json_data['weather'][0]['main']  # Selecting Required INFO.
    temp = int(json_data['main']['temp'] - 273.15)
    min_temp = int(json_data['main']['temp_min'] - 273.15)
    max_temp = int(json_data['main']['temp_max'] - 273.15)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']
    sunrise = time.strftime("%I:%M:%S", time.gmtime(json_data['sys']['sunrise'] - 21600))
    sunset = time.strftime("%I:%M:%S", time.gmtime(json_data['sys']['sunset'] - 21600))

    final_info = condition + "\n" + str(temp) + "°C"
    final_data = "\n" + "Max Temp:" + str(max_temp) + "\n" + "Min Temp:" + str(min_temp) + "\n" + "Pressure:" + str(pressure) + "\n" + "Humidity:" + str(humidity) +"\n" + "Wind Speed:" + str(wind) + "\n" + "Sunrise:" + str(sunrise) + "\n" + "Sunset:" + str(sunset)
    label1.config(text=final_info)
    label2.config(text=final_data)


# Defining UI
canvas = tk.Tk()
canvas.geometry("600x500")  # Geometry of Canvas
canvas.title("Weather App")  # Canvas Title

# Fonts
f = ("poppins", 15, "bold")
t = ("poppins", 35, "bold")

# TextField - (to get city name from users)
textfield = tk.Entry(canvas, font=t)
textfield.pack(pady=20)    # Padding to the Y- Coordinate
textfield.focus()       # TextField will be on Focus Always
textfield.bind('<Return>', getWeather)

# Labels to show Data
label1 = tk.Label(canvas, font=t)
label1.pack()
label2 = tk.Label(canvas, font=f)
label2.pack()

canvas.mainloop()