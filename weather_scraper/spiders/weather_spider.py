import scrapy
from datetime import datetime
import csv

class WeatherSpider(scrapy.Spider):
    name = 'weather'

    def __init__(self, date=None, weather_station=None, *args, **kwargs):
        super(WeatherSpider, self).__init__(*args, **kwargs)
        self.weather_station = weather_station
        self.date = datetime.strptime(date, '%Y-%m-%d').date()

    def start_requests(self):
        date_str = self.date.strftime('%Y-%m-%d')
        url = f'https://www.wunderground.com/dashboard/pws/{self.weather_station}/table/{date_str}/{date_str}/daily'
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        rows = response.xpath('.//lib-history-table/div/div/div/table/tbody/tr')
        extracted_data = []
        for row in rows:
            time = row.xpath('.//td[1]/strong/text()').get()
            temperature = row.xpath('.//td[2]//span/text()').get()
            dew_point = row.xpath('.//td[3]//span/text()').get()
            humidity = row.xpath('.//td[4]//span/text()').get()
            wind = row.xpath('.//td[5]/strong/text()').get()
            speed = row.xpath('.//td[6]//span/text()').get()
            gust = row.xpath('.//td[7]//span/text()').get()
            pressure = row.xpath('.//td[8]//span/text()').get()
            precip_rate = row.xpath('.//td[9]//span/text()').get()
            precip_accum = row.xpath('.//td[10]//span/text()').get()
            uv = row.xpath('.//td[11]/strong/text()').get()
            solar = row.xpath('.//td[12]/strong/text()').get()

            extracted_data.append({
                'Time': time,
                'Temperature': temperature,
                'Dew Point': dew_point,
                'Humidity': humidity,
                'Wind': wind,
                'Speed': speed,
                'Gust': gust,
                'Pressure': pressure,
                'Precip. Rate.': precip_rate,
                'Precip. Accum.': precip_accum,
                'UV': uv,
                'Solar': solar,
            })

        # Define the CSV file name using the start and end dates
        csv_filename = f'{self.weather_station}_{self.date.isoformat()}.csv'

        if not extracted_data:
            print("Couldn't read any data!")
            return

        with open(csv_filename, 'w', newline='') as csvfile:
            fieldnames = extracted_data[0].keys()
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for data in extracted_data:
                writer.writerow(data)
