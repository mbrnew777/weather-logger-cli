# main.py

from weather_fetcher import fetch_and_log_weather
from analyzer import view_logs, city_wise_avg_temp, show_extremes, recent_extremes
from plotter import plot_temperature_trend
from data_handler import load_data, save_data

def menu():
    while True:
        print("\n=== Weather Analyzer CLI ===")
        print("1. Fetch and log weather for cities")
        print("2. View all logs (as table)")
        print("3. Get city-wise average temperature")
        print("4. Show hottest and coldest cities (overall)")
        print("5. Show hottest and coldest cities (last 24h)")
        print("6. Plot temperature trend for a city")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            cities = input("Enter comma-separated city names: ").split(",")
            cities = [c.strip() for c in cities]
            fetch_and_log_weather(cities)
        elif choice == '2':
            view_logs()
        elif choice == '3':
            city_wise_avg_temp()
        elif choice == '4':
            show_extremes()
        elif choice == '5':
            recent_extremes()
        elif choice == '6':
            city = input("Enter city name: ").strip()
            plot_temperature_trend(city)
        elif choice == '7':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again!")

# 🔥 This line is VERY IMPORTANT
if __name__ == "__main__":
    menu()
