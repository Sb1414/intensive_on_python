import sys
import requests
import re


def is_valid_ip(ip):
    ip_pattern = r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$"
    return re.match(ip_pattern, ip) is not None


def get_country_by_ip(ip):
    if not is_valid_ip(ip):
        raise ValueError("Ошибка: Неправильный формат IP-адреса")

    url = f"http://ip-api.com/json/{ip}"
    response = requests.get(url)

    if response.status_code != 200:
        raise Exception("Ошибка: Невозможно получить данные для указанного IP")

    data = response.json()
    if data['status'] != 'success':
        raise Exception("Ошибка: Невозможно определить страну для данного IP")

    return data['country']


def test_city1():
    print("Тест 1:")
    print(get_country_by_ip("24.0.0.0"))


def test_city2():
    print("Тест 1:")
    print(get_country_by_ip("24.48.0.1"))


if __name__ == "__main__":
    test_city1()
    test_city2()
    if len(sys.argv) != 2:
        print("Используйте: python part1.py IP-адрес")
    else:
        ip = sys.argv[1]
        try:
            country = get_country_by_ip(ip)
            print(country)
        except Exception as e:
            print(e)
