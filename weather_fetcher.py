import aiohttp
import asyncio
import json
from datetime import datetime, timedelta
from data_handler import load_data, save_data

API_KEY = '8f909a3e30832d5957e3cbe6a1148fdb'
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid={}'

def fetch_and_log_weather(cities):
    asyncio.run(fetch_all(cities))

async def fetch_city(session, city):
    url = BASE_URL.format(city, API_KEY)
    async with session.get(url) as resp:
        if resp.status == 200:
            data = await resp.json()
            return parse_weather(data)
        else:
            print(f"[ERROR] Failed to fetch {city}")
            return None

def parse_weather(data):
    city = data['name']
    temp = round(data['main']['temp'] - 273.15, 2)
    desc = data['weather'][0]['description']
    humidity = data['main']['humidity']
    utc_time = datetime.utcnow().isoformat()
    local_time = datetime.now().isoformat()

    return {
        'city': city,
        'temperature_c': temp,
        'description': desc,
        'humidity': humidity,
        'utc_timestamp': utc_time,
        'local_timestamp': local_time
    }

async def fetch_all(cities):
    existing = load_data()
    async with aiohttp.ClientSession() as session:
        tasks = []
        for city in cities:
            if not is_duplicate(city, existing):
                tasks.append(fetch_city(session, city))
        results = await asyncio.gather(*tasks)
        for r in results:
            if r:
                existing.append(r)
        save_data(existing)

def is_duplicate(city, existing):
    now = datetime.utcnow()
    for entry in reversed(existing):
        if entry['city'].lower() == city.lower():
            t = datetime.fromisoformat(entry['utc_timestamp'])
            if (now - t) < timedelta(hours=2):
                print(f"[SKIPPED] {city} fetched within last 2 hours.")
                return True
            break
    return False
