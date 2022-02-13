import requests
city = "Moscow,RU"
appid = "44ee527170b2c457771345fc7b59c66c"


res = requests.get("http://api.openweathermap.org/data/2.5/weather",
    params={'q': city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
data = res.json()


print("Город:", city)
print("Погодные условия:", data['weather'][0]['description'])
print("Температура:", data['main']['temp'])
print("Скорость ветра:", data['wind']['speed'])
print("Видимость:", data['visibility'])
print("Минимальная температура:", data['main']['temp_min'])
print("Максимальная температура", data['main']['temp_max'])

print(" ")

res = requests.get("http://api.openweathermap.org/data/2.5/forecast",
    params={'q': city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
data = res.json()

print("Прогноз погоды на неделю:")
for i in data['list']:
    print("Дата:", i['dt_txt'], " \r\nТемпература:",
'{0:+3.0f}'.format(i['main']['temp']), " \r\nПогодные условия:",
i['weather'][0]['description'], " \r\nСкорость ветра:",
i['wind']['speed'], " \r\nВидимость:", i['visibility'] )
    print("____________________________")
