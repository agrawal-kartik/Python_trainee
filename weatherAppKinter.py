import tkinter as tk
from tkinter import messagebox
import requests

# Replace with your actual API key
API_KEY = "71ec1fcdefb328064fa2debf8a1b8021"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def get_weather():
    city = city_entry.get()
    if not city:
        messagebox.showwarning("Input Error", "Please enter a city name.")
        return

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(BASE_URL, params=params)
        data = response.json()

        if response.status_code != 200:
            raise ValueError(data.get("message", "Failed to fetch weather."))

        result = f"""
        City: {data['name']}
        Temperature: {data['main']['temp']}°C
        Description: {data['weather'][0]['description']}
        Humidity: {data['main']['humidity']}%
        Wind Speed: {data['wind']['speed']} m/s
        """
        result_label.config(text=result.strip())
    except Exception as e:
        messagebox.showerror("Error", f"Could not get weather data:\n{e}")


# GUI setup
root = tk.Tk()
root.title("Weather App")
root.geometry("400x300")
root.resizable(False, False)

tk.Label(root, text="Enter City Name:", font=("Arial", 12)).pack(pady=10)
city_entry = tk.Entry(root, font=("Arial", 12), width=30)
city_entry.pack(pady=5)

tk.Button(root, text="Get Weather", font=("Arial", 12), command=get_weather).pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 11), justify="left")
result_label.pack(pady=10)

root.mainloop()