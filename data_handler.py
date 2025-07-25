import json
import os

FILE = "weather_data.json"

def load_data():
    if not os.path.exists(FILE):
        return []
    with open(FILE, 'r') as f:
        return json.load(f)

def save_data(data):
    with open(FILE, 'w') as f:
        json.dump(data, f, indent=2)
