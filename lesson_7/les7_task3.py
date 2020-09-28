import requests
import datetime
from tabulate import tabulate

now = datetime.datetime.now()
city_name = input('Enter city name: ')
days_num = int(input('Number of days: '))
API_KEY = 'f9ada9efec6a3934dad5f30068fdcbb8'

weather_req = requests.get('http://api.openweathermap.org/data/2.5/forecast/daily',
                           params={'q': city_name, 'cnt': days_num, 'units': 'metric', 'lang': 'ru', 'appid': API_KEY})

weather_data = weather_req.json()

f_name = datetime.datetime.now().strftime('%d-%m-%Y') + '-' + str(city_name) + '-'\
         + str(days_num) + '-' + 'days-weather-forecast.txt'
f = open(f_name, 'w+')
f.write(tabulate(None, headers=('Date', 'Day temperature', 'Feels like', 'Night temperature')))
for i in weather_data['list']:
    day_date = datetime.datetime.fromtimestamp(i['dt']).strftime('%d-%m-%Y')
    day_temperature = str(i['temp']['day'])
    feels_like = str(i['feels_like']['day'])
    night_temperature = str(i['temp']['night'])
    table = [day_date, day_temperature, feels_like, night_temperature]
    print(tabulate([table], tablefmt='simple'))
    f.write(tabulate([table], tablefmt='simple'))
