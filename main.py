import requests
from pprint import pprint

appid = '0cb53a3f6e9800a1a8a71e9d8a143f33'

def weather_by_city(city):
    params = {'q': city, 'units': 'metric', 'cnt': '3', 'lang': 'ru', 'APPID': appid}
    result = requests.get('https://api.openweathermap.org/data/2.5/weather', params=params)
    data = result.json()
    if data.get('message') == 'city not found':
        return ("Нет такого города на этой планете!")
    else:
        return(data)

def weather_by_coords(lat,lon):
    params = {'lat': lat, 'lon': lon, 'lang': 'ru', 'APPID': appid}
    result = requests.get('https://api.openweathermap.org/data/2.5/weather', params=params)
    data = result.json()
    if data.get('message') == 'wrong latitude':
        return ("Введите корректные координаты")
    else:
        return(data)

def main():
    print("Выход из программы осуществляется вводом ***")
    while True:
        text = input("Введите наименование населенного пункта или его координаты разделенные символом пробела: ")
        if text == '***':
            break
        elif text[0].isalpha():
            pprint(weather_by_city(text))
        else:
          pprint(weather_by_coords(text.split()[0], text.split()[1]) if text.count(' ') == 1
                 else "Введите корректные координаты")
    print('Всего доброго!')

if __name__ == '__main__':
    main()