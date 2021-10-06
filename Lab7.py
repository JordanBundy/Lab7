import requests
import os
from datetime import datetime

def main():
    key= os.environ.get('WEATHER_KEY')
    url = 'http://api.openweathermap.org/data/2.5/forecast?id=524901&appid='

    location = input('Where would you like the weather for? (city,countrycode(us)): ')

    query = {'q': location, 'units': 'metric', 'appid': key}

    data = requests.get(url, params=query).json()
    #getting the item data from the API
    forecast_items = data['list']
    #looping to create the forecasts to be readable for the use
    for forecast in forecast_items:
        timestamp = forecast['dt']
        date = datetime.fromtimestamp(timestamp)
        temp = forecast['main']['temp']
        print(f'at {date} temp is {temp}')


if __name__ == '__main__':
    main()