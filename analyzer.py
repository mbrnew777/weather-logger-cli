from data_handler import load_data
from datetime import datetime, timedelta
from collections import defaultdict
from tabulate import tabulate

def view_logs():
    data = load_data()
    print(tabulate(data, headers="keys", tablefmt="fancy_grid"))

def city_wise_avg_temp():
    data = load_data()
    temps = defaultdict(list)
    for entry in data:
        temps[entry['city']].append(entry['temperature_c'])
    avg = {city: round(sum(vals)/len(vals), 2) for city, vals in temps.items()}
    print(tabulate(avg.items(), headers=["City", "Avg Temp (°C)"], tablefmt="grid"))

def show_extremes():
    data = load_data()
    sorted_data = sorted(data, key=lambda x: x['temperature_c'])
    print(f"Coldest City: {sorted_data[0]['city']} ({sorted_data[0]['temperature_c']}°C)")
    print(f"Hottest City: {sorted_data[-1]['city']} ({sorted_data[-1]['temperature_c']}°C)")

def recent_extremes():
    data = load_data()
    now = datetime.utcnow()
    recent = [d for d in data if (now - datetime.fromisoformat(d['utc_timestamp'])) <= timedelta(hours=24)]
    if not recent:
        print("No data in last 24 hours.")
        return
    sorted_data = sorted(recent, key=lambda x: x['temperature_c'])
    print(f"[24H] Coldest City: {sorted_data[0]['city']} ({sorted_data[0]['temperature_c']}°C)")
    print(f"[24H] Hottest City: {sorted_data[-1]['city']} ({sorted_data[-1]['temperature_c']}°C)")
