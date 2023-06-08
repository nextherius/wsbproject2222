import matplotlib.pyplot as plt
import requests
from datetime import datetime
from geopy.geocoders import Nominatim
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from io import BytesIO
import base64

class Forecast:
    def __init__(self, city):
        self.city = city
        geolocator = Nominatim(user_agent="MyApp")
        location = geolocator.geocode(f"{city}")
        latitude = location.latitude
        longitude = location.longitude
        api_url = f'https://api.open-meteo.com/v1/forecast?latitude={float(latitude)}&longitude={float(longitude)}&hourly=temperature_2m'
        response = requests.get(api_url)
        if response.status_code == requests.codes.ok:
            self.data = response.json()
        else:
            print("Error Forecast Class :", response.status_code, response.text)

    def get_temp(self):
        return self.data['hourly']['temperature_2m']

    def get_date(self):
        return self.data['hourly']['time']

    def format_datetime(self, datetime_str):
        dt = datetime.fromisoformat(datetime_str)
        return dt.strftime('%Y-%m-%d %H:%M')

    def get_chart_html(self):
        temperature = self.get_temp()
        date = self.get_date()

        formatted_date = [self.format_datetime(dt) for dt in date]

        # Set the dark background style
        plt.style.use('dark_background')

        # Create the plot and customize its appearance
        fig, ax = plt.subplots()
        ax.plot(formatted_date, temperature, color='limegreen', linewidth=2)

        ax.set_xlabel('Time', color='white')
        ax.set_ylabel('Temperature (°C)', color='white')
        ax.set_title(f'Temperature in {self.city}', color='white')

        ax.tick_params(axis='x', colors='white')
        ax.tick_params(axis='y', colors='white')

        # Show only every 6th value on the Y-axis
        ax.yaxis.set_major_locator(plt.MaxNLocator(6))

        plt.xticks(rotation=45)
        plt.tight_layout()

        # Convert the plot to HTML
        canvas = FigureCanvas(fig)
        buffer = BytesIO()
        canvas.print_png(buffer)
        data = buffer.getvalue()

        html = '<img src="data:image/png;base64,' + base64.b64encode(data).decode() + '">'
        return html

Prognoza = Forecast("Wroclaw")
print(Prognoza.get_chart_html())
