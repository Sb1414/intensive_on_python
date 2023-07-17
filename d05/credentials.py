from urllib.parse import parse_qs
from wsgiref.simple_server import make_server

def application(environ, start_response):
    # Получаем параметры GET из URL-адреса
    query = parse_qs(environ['QUERY_STRING'])
    species = query.get('species', [''])[0]

    # Определяем правильные учетные данные в зависимости от вида
    credentials = {
        'Cyberman': 'John Lumic',
        'Dalek': 'Davros',
        'Judoon': 'Shadow Proclamation Convention 15 Enforcer',
        'Human': 'Leonardo da Vinci',
        'Ood': 'Klineman Halpen',
        'Silence': 'Tasha Lem',
        'Slitheen': 'Coca-Cola salesman',
        'Sontaran': 'General Staal',
        'Time Lord': 'Rassilon',
        'Weeping Angel': 'The Division Representative',
        'Zygon': 'Broton'
    }

    # Формируем JSON-ответ в зависимости от наличия учетных данных для указанного вида
    if species in credentials:
        response_body = '{"credentials": "%s"}' % credentials[species]
        status = '200 OK'
    else:
        response_body = '{"credentials": "Unknown"}'
        status = '404 Not Found'

    # Устанавливаем заголовки ответа
    response_headers = [('Content-Type', 'application/json; charset=utf-8')]

    # Отправляем статус и заголовки ответа серверу WSGI
    start_response(status, response_headers)

    # Возвращаем тело ответа в виде списка байтов
    return [response_body.encode()]

# Создаем сервер WSGI
httpd = make_server('localhost', 8888, application)

print("Сервер запущен на http://localhost:8888/...")

# Запускаем сервер
httpd.serve_forever()