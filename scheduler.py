import asyncio
import time
from weather_fetcher import fetch_all

# List of cities to auto-fetch
CITIES = ['delhi', 'mumbai', 'ahmedabad', 'jaipur', 'surat']

# Interval in seconds (e.g., every 5 minutes = 300s)
INTERVAL = 300  

async def scheduled_fetch():
    while True:
        print(f"[Scheduler] Fetching weather for {', '.join(CITIES)}")
        await fetch_all(CITIES)
        print("[Scheduler] Waiting for next run...\n")
        await asyncio.sleep(INTERVAL)

if __name__ == "__main__":
    try:
        asyncio.run(scheduled_fetch())
    except KeyboardInterrupt:
        print("Scheduler stopped.")
