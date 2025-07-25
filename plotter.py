import matplotlib.pyplot as plt
from data_handler import load_data
import os
from datetime import datetime

def plot_temperature_trend(city):
    data = load_data()
    city_data = [d for d in data if d['city'].lower() == city.lower()]
    if not city_data:
        print("No data found for", city)
        return
    times = [datetime.fromisoformat(d['local_timestamp']) for d in city_data]
    temps = [d['temperature_c'] for d in city_data]

    plt.figure(figsize=(10,5))
    plt.plot(times, temps, marker='o')
    plt.title(f"Temperature Trend - {city}")
    plt.xlabel("Time")
    plt.ylabel("Temperature (°C)")
    plt.grid(True)
    os.makedirs("plots", exist_ok=True)
    filename = f"plots/{city.lower()}_temp_trend.png"
    plt.savefig(filename)
    plt.close()
    print(f"Plot saved as {filename}")
