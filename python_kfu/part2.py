# import requests
# from bs4 import BeautifulSoup
#
# # Отправляем GET-запрос на страницу погоды
# url = 'https://yandex.ru/pogoda'
# response = requests.get(url)
#
# # Парсим HTML страницы
# soup = BeautifulSoup(response.text, 'html.parser')
#
# # Получаем информацию о погоде на сегодня
# today_weather = soup.find('div', class_='fact')
# temperature = today_weather.find('span', class_='temp__value').text
# condition = today_weather.find('div', class_='link__condition').text


# print(f'Погода на сегодня: Температура {temperature}, {condition}')

# # Получаем информацию о погоде на неделю
# week_weather = soup.find('div', class_='forecast-briefly')
# days = week_weather.find_all('div', class_='forecast-briefly__day')
# for day in days:
#     date = day.find('time', class_='forecast-briefly__date').text
#     temp = day.find('div', class_='temp forecast-briefly__temp').text
#     condition = day.find('div', class_='forecast-briefly__condition').text
#     print(f'На {date}: Температура {temp}, {condition}')

import requests
from bs4 import BeautifulSoup

url = 'https://yandex.ru/pogoda/?from=main_portal'
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    temperature_elem = soup.find('span', class_='temp__value temp__value_with-unit')

    if temperature_elem:
        temperature = temperature_elem.get_text()
        print(f'Текущая температура: {temperature}')
    else:
        print('Элемент с классом "temp__value temp__value_with-unit" не найден на странице.')
else:
    print('Ошибка: Невозможно получить данные.')
