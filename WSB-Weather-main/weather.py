import datetime
import requests
from datetime import datetime


class Weather:
    def __init__(self, city):
        self.city = city
        api_url = 'https://api.api-ninjas.com/v1/weather?city={}'.format(city)
        response = requests.get(api_url, headers={'X-Api-Key': 'jXWlaMLXiXssi9FBSqEJKA==m5a7a0cLHGQZtdb7'})
        if response.status_code == requests.codes.ok:
            print(response.text)
        else:
            print("Error Weather Class :", response.status_code, response.text)
    def get_humidity(self):
        humidity = self.data.get('humidity')
        return humidity

    def get_temp(self):
        temp = self.data.get('temp')
        return temp

    def get_sunrise(self):
        sunrise_times = self.data.get('sunrise')
        sunrise_time = datetime.datetime.fromtimestamp(sunrise_times).strftime("%Y-%m-%d %H:%M:%S")
        return sunrise_time

    def get_sunset(self):
        sunset_times = self.data.get('sunset')
        sunset_time = datetime.datetime.fromtimestamp(sunset_times).strftime("%Y-%m-%d %H:%M:%S")
        return sunset_time

    def get_wind(self):
        wind = self.data.get('wind_speed')
        return wind






#Pogoda = Weather("Żary")


