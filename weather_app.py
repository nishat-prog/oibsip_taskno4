import requests
import json

def get_weather(api_key, location):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric'
    response = requests.get(url)
    data = response.json()
    return data

def display_weather(data):
    if data['cod'] != '404':
        main = data['main']
        weather = data['weather'][0]
        temperature = main['temp']
        humidity = main['humidity']
        description = weather['description']

        print(f'Temperature: {temperature}°C')
        print(f'Humidity: {humidity}%')
        print(f'Weather: {description}')
    else:
        print('Location not found.')

if __name__ == '__main__':
    api_key = 'c89f30dfce904fd91bfd2115ed5791d9' 
    location = input('Enter city name or ZIP code: ')
    weather_data = get_weather(api_key, location)
    display_weather(weather_data)
