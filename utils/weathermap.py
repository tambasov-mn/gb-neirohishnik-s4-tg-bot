# http://api.openweathermap.org/
import requests

#
def show_weather_msk():
    url = 'http://api.openweathermap.org/data/2.5/weather?q=moscow&appid=15950a39afdf3fa7600bc9ef74c4a62c&units=metric&lang=ru'
    response = requests.get(url)

    if response.status_code:
        data = response.json()['main']
        temp = data['temp']
        weather = str(temp)
        return weather

def show_weather_spb():
    url = 'http://api.openweathermap.org/data/2.5/weather?q=Saint Petersburg&appid=15950a39afdf3fa7600bc9ef74c4a62c&units=metric&lang=ru'
    response = requests.get(url)
    # 498817
    # SaintPetersburg
    if response.status_code:
        data = response.json()['main']
        temp = data['temp']
        weather = str(temp)
        return weather

#
if __name__ == '__main__':
    print(show_weather_msk())
    print(show_weather_spb())

