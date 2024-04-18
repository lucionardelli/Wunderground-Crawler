# Weather Data Scraper

This is a Scrapy spider designed to scrape weather data from this site: https://www.wunderground.com/dashboard/pws/

## Setup

### 0. Prerquisites
User should have `git` and `pip` installed already and must be familiar (or brave enough!) with using the terminal.

### 1. Clone the Repository

```bash
git clone https://github.com/lucionardelli/weather-scraper.git
cd weather-scraper
```

### 2. Create a Python Virtual Environment
It's recommended to use a virtual environment to manage dependencies.

# Install virtualenv if you haven't already
```bash
pip install virtualenv
```

# Create a virtual environment
```bash
virtualenv wunderground-crawler
```

# Activate the virtual environment
# For Windows
```bash
wunderground-crawler\Scripts\activate
```

# For macOS/Linux
```bash
source wunderground-crawler/bin/activate
```

### 3. Install Scrapy
In the same terminal you run the previous command:
```bash
pip install scrapy
```

4. Run the Spider
Make sure you are in the project's directory (where the spider code is located).

```bash
cd weather_spider
```

# Run the spider with date and weather station code
k
```bash
scrapy crawl weather -a date=2024-03-29 -a weather_station=IROSAR97
```

This will generate a `.csv` file in the project's root directory named `IROSAR97_2024-03-29.csv`
