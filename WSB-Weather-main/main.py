from flask import Flask, render_template, request
import requests
from weather import Weather
import news
import forecast


app = Flask(__name__)

def get_weather(city):
    api_key = 'YOUR_API_KEY'  # Replace with your OpenWeatherMap API key
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    response = requests.get(url)
    data = response.json()
    return data

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/weather', methods=['POST'])
def weather():
    city = request.form['city']
    data = get_weather(city)

    if data['cod'] == '404':
        message = 'City not found!'
        return render_template('index.html', message=message)

    weather_desc = data['weather'][0]['description']
    temp = round(data['main']['temp'] - 273.15, 2)  # Convert temperature from Kelvin to Celsius

    return render_template('weather.html', city=city, weather_desc=weather_desc, temp=temp)

if __name__ == '__main__':
    app.run()