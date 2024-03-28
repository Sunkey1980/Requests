import requests
from pprint import pprint

city = 'Оренбург'
appid = '0cb53a3f6e9800a1a8a71e9d8a143f33'
params={'q': city, 'units': 'metric','cnt':'3','lang': 'ru', 'APPID': appid}

def weather_by_city(city):
    params = {'q': city, 'units': 'metric', 'cnt': '3', 'lang': 'ru', 'APPID': appid}
    result = requests.get('https://api.openweathermap.org/data/2.5/weather', params=params)
    data = result.json()
    return(data)

def weather_by_coords(lat,lon):
    params = {'lat': lat, 'lon': lon, 'lang': 'ru', 'APPID': appid}
    result = requests.get('https://api.openweathermap.org/data/2.5/weather', params=params)
    data = result.json()
    return(data)

def main():
    text = input("Введите наименование населенного пункта или его координаты разделенные символом пробела: ")
    if text.isalpha():
        pprint(weather_by_city(text))
    else:
        pprint(weather_by_coords(text.split()[0], text.split()[1]))


if __name__ == '__main__':
    main()