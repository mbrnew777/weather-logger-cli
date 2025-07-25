
# 🌦️ Asynchronous Weather Logger & Analyzer with Caching and Visualization

A Python CLI tool that asynchronously fetches real-time weather data for multiple cities using the OpenWeatherMap API. It logs, analyzes, and visualizes weather trends over time with support for caching and scheduled updates.

---

## 🚀 Features

- ✅ Asynchronous API calls using `aiohttp` and `asyncio`
- ✅ Logs data to `weather_data.json` with timestamp
- ✅ Prevents duplicate entries within a 2-hour window per city
- ✅ CLI Menu for various analysis options
- ✅ View all-time and last-24-hour hottest/coldest cities
- ✅ City-wise average temperature calculation
- ✅ Plots temperature vs time using `matplotlib`
- ✅ Optional scheduler for auto-fetching weather data

---

## 🔧 Project Run Instructions

1. **Clone the Repository**  
   ```bash
   git clone https://github.com/your-username/weather-logger.git
   cd weather-logger
   ```

2. **Install Required Packages**  
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up Environment Variable (API Key)**  
   Create a `.env` file in the root directory and add:
   ```
   API_KEY=your_openweathermap_api_key
   ```

4. **Run the CLI Tool**
   ```bash
   python main.py
   ```

5. **Optional: Run the Scheduler to Auto-Log Weather Every Hour**
   ```bash
   python scheduler.py
   ```

---

## 🔑 How to Generate OpenWeatherMap API Key

1. Visit: https://home.openweathermap.org/users/sign_up  
2. Sign up and verify your email.  
3. Go to the **API Keys** section in your dashboard.  
4. Copy the default API key provided.  
5. Paste it into the `.env` file like:
   ```
   API_KEY=your_api_key_here
   ```

---

## 🧪 Sample CLI Options

```text
=== Weather Analyzer CLI ===

1. Fetch and log weather for cities
2. View all logs (as table)
3. Get city-wise average temperature
4. Show hottest and coldest cities (overall and in last 24h)
5. Plot temperature trend for a city
6. Exit
```

---

## 🗂 Project Structure

```
.
├── main.py               # Entry-point CLI logic
├── fetcher.py            # Asynchronous API logic
├── analyzer.py           # Analysis tools
├── plotter.py            # Matplotlib plotting
├── scheduler.py          # Auto-fetch scheduler
├── utils.py              # Utilities
├── weather_data.json     # Logged data
├── plots/                # Saved graph images
├── .env                  # API Key (not committed)
├── .gitignore
└── README.md
```

---

## 📌 Assumptions and Extra Features

### Assumptions:
- Each city will be logged no more than once every **2 hours** to avoid duplicate spam.
- Temperature is converted from **Kelvin to Celsius** before storage.
- Data is stored in a flat JSON file (`weather_data.json`), though extendable to SQLite.

### Extra Features:
- ⏱ Scheduler (`scheduler.py`) to fetch data at regular intervals (e.g., every hour)
- 📉 Plot generation for each city and save to `plots/` directory
- 🌐 Optional flag support using `argparse` for CLI automation
- 🔄 Can be extended to use a **React frontend** for visual dashboard

---

## ✅ Submission Checklist

- [x] At least 10 entries in `weather_data.json`
- [x] Plot file saved under `plots/`
- [x] All CLI menu options implemented
- [x] README with run instructions, API key setup, assumptions

---

## 👨‍💻 Author

**Meet Raval**  
Backend Developer | Python & Django Expert  
GitHub: [your-username]
