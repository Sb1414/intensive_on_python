# intensive_on_python
решение задач на python

# Оглавление
1. [День 00](#день-00) \
    [Упражнение 00: Блокчейн](#упражнение-00-блокчейн)\
    [Упражнение 01: Расшифровка](#упражнение-01-расшифровка)\
    [Упражнение 02. Отслеживание и захват](#упражнение-02-отслеживание-и-захват)
2. [День 01](#день-01)\
    [Упражнение 00: Функциональный кошелек](#упражнение-00-функциональный-кошелек)\
    [Упражнение 01: Расщепление](#упражнение-01-расщепление)\
    [Упражнение 02: Охранная сигнализация](#упражнение-02-охранная-сигнализация)
3. [День 02](#день-02)\
    [Упражнение 00: Получение доступа](#упражнение-00-получение-доступа)\
    [Упражнение 01: Мораль](#упражнение-01-мораль)
4. [День 03](#день-03)\
    [Упражнение 00: Невинная шутка](#упражнение-00-невинная-шутка)\
    [Упражнение 01: Денежный поток](#упражнение-01-денежный-поток)
5. [День 04](#день-04)\
    [Упражнение 00: Поток энергии](#упражнение-00-поток-энергии)\
    [Упражнение 01: Личности](#упражнение-01-личности)\
    [Упражнение 02: Противодавление](#упражнение-02-противодавление)
6. [День 05](#день-05)\
    [Упражнение 00: Обмани меня один раз](#упражнение-00-обмани-меня-один-раз)\
    [Упражнение 01: Песня про отвертку](#упражнение-01-песня-про-отвертку)\
    [Упражнение 02. Правильное время](#упражнение-02-правильное-время)
7. [День 06](#день-06)\
    [Упражнение 00: Отчет по Кирову](#упражнение-00-отчет-по-кирову)\
    [Упражнение 01. Качество данных](#упражнение-01-качество-данных)\
    [Упражнение 02: Ведение записей](#упражнение-02-ведение-записей)
8. [День 07](#день-07)\
    [Упражнение 00: Пенсионный план](#упражнение-00-пенсионный-план)\
    [Упражнение 01: Человеческая жизнь](#упражнение-01-человеческая-жизнь)\
    [Упражнение 02: На будущее](#упражнение-02-на-будущее)
9. [День 08](#день-08)\
    [Упражнение 00: Я знаю кунг-фу](#упражнение-00-я-знаю-кунг-фу)\
    [Упражнение 01: Кальмар на палочке](#упражнение-01-кальмар-на-палочке)\
    [Упражнение 02: Дежавю](#упражнение-02-дежавю)
10. [День 09](#день-09)\
    [Упражнение 00: все еще считается](#упражнение-00-все-еще-считается)\
    [Упражнение 01. Доля секунды](#упражнение-01-доля-секунды)\
    [Упражнение 02: Автопилот](#упражнение-02-автопилот)

11. [Задания от КФУ]()

# День 00
## Упражнение 00: Блокчейн
Дан [файл](d00/data_hashes_10lines.txt), с несколькими строками. Некоторые строки начинаются с нескольких нулей. Нужно написать Python-скрипт, который сможет получать текст со своего стандартного ввода, а затем выводить только те строки, которые начинаются ровно с 5 нулей и строка имеет длину 32 символа. Строка, начинающаяся с 6 нулей, НЕ считается правильной.

Код должен принимать количество строк в качестве аргумента, например:
```
~$ cat data_hashes_10lines.txt | python blocks.py 10
```
Таким образом, программа остановится, когда обработает 10 строк. 

## Упражнение 01: Расшифровка
Электронные письма состояли из каких-то странных текстов, таких как "The only way everyone reaches Brenda rapidly is delivering groceries explicitly" или "Britain is Great because everyone necessitates". Написать скрипт на Python, который можно использовать для расшифровки подобных сообщений и распечатать ответ одним словом без пробелов. Он должен запускаться следующим образом:
```
~$ python decypher.py \"Have you delivered eggplant pizza at restored keep?\"
```

## Упражнение 02. Отслеживание и захват
В качестве входных данных коду дается двумерное «изображение» в виде текста в файле m.txt. Файл содержит пять символов в трех строках, например:
```
*d&t*
**h**
*l*!*
```
Есть шаблон из звезд с буквой M. Все, что нужно сделать — это напечатать «True», если этот M-шаблон существует в заданном входном изображении, или «False» в противном случае. Другие символы (за пределами шаблона M) должны быть другими, поэтому в примере должно быть напечатано «False»:
```
*****
*****
*****
```
Если данный шаблон не 3x5, то вместо него должно быть напечатано слово «Error». Файл с кодом должен называться mfinder.py.

# День 01
## Упражнение 00: Функциональный кошелек
нужно написать функции `add_ingot(purse)`, `get_ingot(purse)`которые `empty(purse)` принимают кошелек (словарь, строго говоря, a `typing.Dict[str, int]`) и возвращают кошелек (пустой dict в случае `empty(purse)`).

Объект, переданный в качестве аргумента, не должен изменяться внутри функции. Вместо этого должен быть возвращен новый объект. Вы должны вернуть *новый экземпляр dict* с обновленным номером внутри него.

Композиция функций вроде `add_ingot(get_ingot(add_ingot(empty(purse))))` должна возвращать `{\"gold_ingots\": 1}`. Кроме того, получение слитка из пустого кошелька не должно приводить к ошибке и должно просто возвращать пустой кошелек.

Примечание: в этой задаче нас интересуют только золотые слитки, так что не имеет особого значения, что будет с остальными вещами внутри кошелька. Вы можете сохранить его или выбросить.

## Упражнение 01: Расщепление
Написать функцию с именем `split_booty`, которая будет принимать любое количество кошельков (словарей) в качестве аргументов. Количество слитков может быть нулевым или целым положительным числом.

Эта функция должна вернуть назад три кошелька (словаря) так, чтобы в любых двух из трех кошельков разница между количеством слитков была не больше 1. Например, если в добыче есть , и , то `{"gold_ingots":3}` функция `{"gold_ingots":2}` должна `{"apples":10}` вернуть `({"gold_ingots": 2}, {"gold_ingots": 2}, {"gold_ingots": 1})`.

При реализации этой функции вы все равно не должны использовать прямое присвоение полей внутри словарей. Вместо этого вы можете повторно использовать функции, которые вы написали в EX00.

## Упражнение 02: Охранная сигнализация
Вы написали несколько функций (`add_ingot(purse), get_ingot(purse)и empty(purse)`) для дизайна кошелька, но теперь вам нужно придумать способ добавить какое-то новое поведение ко всем из них — всякий раз, когда вызывается какая-либо из них, `SQUEAK` должно быть напечатано слово. Хитрость в том, что вы не можете изменить тело этих функций, но по-прежнему выдаете этот аларм. Подсказка: нужно использовать [decorator](<https://realpython.com/primer-on-python-decorators/>).

# День 02
## Упражнение 00: Получение доступа
```
AssertionError: len(key) == 1337
AssertionError: key[404] == 3
AssertionError: key > 9000
AssertionError: key.passphrase == "zax2rulez"
AssertionError: str(key) == "GeneralTsoKeycard"
```
Нужно описать класс Python `Key` так, чтобы экземпляр этого класса прошел перечисленные выше проверки. Имейте в виду, что ваш код в этом упражнении не должен создавать никаких контейнеров ни размером 404, ни меньше. Даже без него вы сможете пройти эти проверки.

Вам рекомендуется написать фактический набор тестов для имитации проверки ключей в соответствии с приведенными выше ошибками (и для упрощения экспертной проверки). Это оценивается как бонус.

## Упражнение 01: Мораль
Написать игру, как [эта](<https://ncase.me/trust/>)

# День 03
## Упражнение 00: Невинная шутка
Файл [evilcorp.html](d03/materials/evilcorp.html) в общей папке. Можно запустить `python3 -m http.server` этот файл в каталоге, чтобы протестировать в браузере. Просто открыть http://127.0.0.1:8000/evilcorp.html .
Вот скрипт, который нужно было внедрить на веб-страницу:
``` 
<script>
        hacked = function() {
            alert('hacked');
        }
        window.addEventListener('load', 
          function() { 
            var f = document.querySelector("form");
            f.setAttribute("onsubmit", "hacked()");
          },
          false
        );
</script>
```
Нужно написать скрипт «exploit.py», который будет делать:
- изменить заголовок страницы (в `<title>` тегах) на «Evil Corp - Stealing your money every day».
- проанализировать имя пользователя со страницы (включая местоимение) и вставить новый тег `<h1>`
в a bodyстраницы, говоря `<h1>` Mr. Robot, you are hacked!`</h1>`
- внедрить скрипт Трентона в страницу
- ссылка в нижней части страницы теперь должна вести на « https://mrrobot.fandom.com/wiki/Fsociety » с фактическим названием компании на странице, замененным на «Fsociety».

Новый HTML-файл должен называться «evilcorp_hacked.html» и размещаться в том же каталоге, что и исходный файл «evilcorp.html».

## Упражнение 01: Денежный поток
нужно написать два скрипта - `producer.py` и `consumer.py`.
Производитель должен генерировать сообщения JSON следующим образом:
```
{
   "metadata": {
       "from": 1023461745,
       "to": 5738456434
   },
   "amount": 10000
}
```

# День 04
## Упражнение 00: Поток энергии
написать скрипт `energy.py` с функцией с именем `fix_wiring()`, которая должна принимать три итерации (вы можете проверить функциональность только с помощью списков) с именами `cables`, `sockets` и `plugs`. Эта функция не должна делать никаких предположений о длине этих итераций, которые могут быть разными. Он должен возвращать другую итерацию по строкам с такими командами, как:

`plug cable1 into socket1 using plug1` `weld cable2 to socket2 without plug`

Для такого кода:
```
plugs = ['plug1', 'plug2', 'plug3']
sockets = ['socket1', 'socket2', 'socket3', 'socket4']
cables = ['cable1', 'cable2', 'cable3', 'cable4']

for c in fix_wiring(cables, sockets, plugs):
    print(c)
```
вывод должен быть:
```
plug cable1 into socket1 using plug1
plug cable2 into socket2 using plug2
plug cable3 into socket3 using plug3
weld cable4 to socket4 without plug
```

## Упражнение 01: Личности
```
class: Turret
personality traits: neuroticism, openness, conscientiousness, extraversion, agreeableness
actions: shoot, search, talk
```

Нужно реализовать функцию генератора для турелей, вызываемую `turrets_generator()`в файле с именем `personality.py`. Вам не следует описывать класс Turret отдельно (есть способ динамически сгенерировать как класс, так и экземпляр, `class` вообще не используя это слово).

Кроме того, три метода должны просто печатать "Shooting", "Searching" и "Talking" соответственно. Каждая черта личности должна быть случайным числом от 0 до 100, а сумма всех пяти для каждого экземпляра должна быть равна 100.

## Упражнение 02: Противодавление
Нужно создать файл `pressure.py` функции-генератора `emit_gel()`. Он должен генерировать бесконечный поток чисел от 50 до 100 (значения > 100 считаются ошибкой) со случайным шагом, выбранным из диапазона `[0, step]` где `step` аргумент генератора `emit_gel()`.

Если генератор в какой-то момент выдает значение ниже 20 или выше 80, следует применить действие, которое изменит знак шага. Чтобы реализовать такой клапан, вам нужно написать еще одну функцию с именем `valve()`, которая будет перебирать значения `emit_gel()` и использовать `.send()` метод для изменения знака текущего шага.

Если давление выше 90 или ниже 10, `emit_gel()` генератор должен быть корректно закрыт, а скрипт должен выйти.

# День 05
## Упражнение 00: Обмани меня один раз
Нужно реализовать сервер [WSGI](<https://wsgi.tutorial.codepoint.net/intro>) с оболочкой HTTP без использования каких-либо внешних зависимостей. Он должен прослушивать локальный порт 8888 и анализировать параметры GET из URL-адреса для любого названия вида, возвращающего вам JSON (это должен быть HTTP-код 200, также обратите внимание на соответствующий заголовок «Content-Type» и кодировку URL). Пример использования cURL может выглядеть так:
```
~$ curl http://127.0.0.1:8888/?species=Time%20Lord
{"credentials": "Rassilon"}
```
Если он не знает переданный вид, он должен вернуться `{"credentials": "Unknown"}` вместе с кодом состояния HTTP 404.

Все приложение для этой задачи должно состоять из одного файла `credentials.py`.

## Упражнение 01: Песня про отвертку
Нужно создать простое клиент-серверное приложение WSGI+HTTP для управления звуковыми файлами.

Во-первых, сервер. Он не должен использовать какую-либо базу данных, достаточно просто хранить файлы на диске. Веб-интерфейс должен работать на порту 8888. При открытии веб-страницы должен отображаться список уже загруженных звуковых файлов, а также кнопка для загрузки еще одного. Как пользователь, вы должны иметь возможность нажать на эту кнопку, загрузить файл на сервер, и он должен появиться в списке файлов, показанных на веб-странице.

Кроме того, сервер должен выполнять проверку [типа MIME](<https://en.wikipedia.org/wiki/Media_type>), поэтому принимаются только аудиофайлы (например `mp3`, `ogg` и `wav`). Если загружается не аудиофайл (например `jpg`, `exe` или `docx`), его следует удалить, а на веб-странице должно появиться сообщение «Обнаружен не аудиофайл». Можно реализовать воспроизведение загруженных звуковых файлов прямо с веб-страницы.

Для этой задачи рекомендуется использовать фреймворк [Flask](<https://flask.palletsprojects.com/en/2.3.x/>) или [Django](<https://www.djangoproject.com/>), это не является строгим требованием. Добавить в файл любые сторонние зависимости, которые вы использовали `requirements.txt`. Также включите файл `README`, объясняющий, как запустить HTTP-сервер (он должен содержать конкретную команду для запуска).

Это должно быть приложение командной строки с двумя возможными действиями:

- `python screwdriver.py upload /path/to/file.mp3` следует загрузить локальный аудиофайл `/path/to/file.mp3` на сервер
- `python screwdriver.py list` должен получить и распечатать имена всех файлов, присутствующих в данный момент на сервере.

Все взаимодействие между клиентом и сервером должно осуществляться по протоколу HTTP. Рекомендуется (хотя и не является строго обязательным) использовать библиотеку [Requests](<https://docs.python-requests.org/en/latest/>) или [HTTPX](<https://www.python-httpx.org/>) для выполнения HTTP-запросов.

## Упражнение 02. Правильное время
У каждого Доктора в **правой** руке есть отвертка, но для действия требуется **минимум две**. Итак, чтобы получить два сразу, Доктор должен взять отвертку у другого Доктора слева. Но если это сделают все, то ничего особо не изменится, так как у каждого врача останется по одной отвертке.

Начните с представления врачей и отверток в виде классов Python. Врачи пронумерованы от 9 до 13, и каждый из них должен сделать один взрыв двумя отвертками. Сам код должен быть в файле `doctors.py`.

*ПРИМЕЧАНИЕ:* это вариант известной задачи параллельного программирования, обычно называемой ["Обед философов"](<https://en.wikipedia.org/wiki/Dining_philosophers_problem>).

# День 06
## Упражнение 00: Отчет по Кирову
Основной протокол, используемый для межпространственной связи, назывался **«Protobuf 2.0»**. Записи отправлялись через транспорт под названием **«gRPC»**.

Поскольку gRPC — это инфраструктура связи клиент-сервер, необходимо было реализовать два компонента — «reporting_server.py» и «reporting_client.py». Сервер должен предоставить конечную точку потоковой передачи ответов, где он получает набор координат (Эндеру было разрешено использовать [любую конкретную систему](<https://en.wikipedia.org/wiki/Astronomical_coordinate_systems>), которая ему нравится), и отвечает потоком записей космического корабля.

Поскольку в настоящее время это тестовая среда, хотя каждый космический корабль должен иметь все упомянутые параметры, они могут быть случайными.

Количество офицеров на борту — случайное число от 0 (только для вражеских кораблей) до 10.

Рабочий процесс должен быть таким:
1. сервер запущен
2. клиент запускается с заданным набором координат в выбранной форме, например:

`~$ ./reporting_client.py 17 45 40.0409 −29 00 28.118`

Все полученные данные отправляются в виде набора сериализованных строк JSON, например:
```
{
  "alignment": "Ally",
  "name": "Normandy",
  "class": "Corvette",
  "length": 216.3,
  "crew_size": 8,
  "armed": true,
  "officers": [{"first_name": "Alan", "last_name": "Shepard", "rank": "Commander"}]
}
{
  "alignment": "Enemy",
  "name": "Executor",
  "class": "Dreadnought",
  "length": 19000.0,
  "crew_size": 450,
  "armed": true,
  "officers": []
}
```

## Упражнение 01. Качество данных
Список классов с определенными параметрами:
| Class       | Length     | Crew    | Can be armed? | Can be hostile? |
|-------------|------------|---------|---------------|-----------------|
| Corvette    | 80-250     | 4-10    | Yes           | Yes             |
| Frigate     | 300-600    | 10-15   | Yes           | No              |
| Cruiser     | 500-1000   | 15-30   | Yes           | Yes             |
| Destroyer   | 800-2000   | 50-80   | Yes           | No              |
| Carrier     | 1000-4000  | 120-250 | No            | Yes             |
| Dreadnought | 5000-20000 | 300-500 | Yes           | Yes             |

Представить эти ограничения в виде типов данных [Pydantic](<https://pydantic-docs.helpmanual.io/usage/models/>). 

Таким образом будет не только проще проверять входящие данные, но и сериализация в JSON станет намного проще. Решил сделать другую версию клиента ("reporting_client_v2.py"), которая будет работать с этим же сервером. Но на этот раз он должен проверить поток космических кораблей с помощью Pydantic и отфильтровать те, у которых некоторые параметры выходят за пределы, в соответствии с таблицей выше. Остальное должно быть напечатано точно так же, как в EX00.

Кроме того, Name может быть «Unknown» ТОЛЬКО для вражеских кораблей.

## Упражнение 02: Ведение записей
Для последнего слоя Хранилища должно было быть еще одно представление Космического корабля, теперь уже в виде ОРМ-модели.

Теперь проект должен будет включать скрипт «reporting_client_v3.py», который отвечает за сопоставление входящих объектов с базой данных через ORM.

Третья версия клиента теперь должна не только распечатывать отфильтрованный список космических кораблей, но и сохранять их в базе данных PostgreSQL (избегая хранения дубликатов, т.к. Имя в сочетании с набором офицеров является уникальной комбинацией).

Интерфейс сканирования в версии 3 должен выглядеть так (обратите внимание на слово «сканировать»):

`~$ ./reporting_client.py scan 17 45 40.0409 −29 00 28.118`

И список предателей был бы

`~$ ./reporting_client.py list_traitors`

который должен напечатать список строк JSON с именами «предателей»:
```
{"first_name": "Lando", "last_name": "Calrissian", "rank": "Entrepreneur"}
{"first_name": "Red", "last_name": "Guy", "rank": "Impostor"}
```
ДОПОЛНИТЕЛЬНЫЙ БОНУС: подумать о том, что произойдет, если формат хранения изменится. Попробуйте использовать [Alembic](<https://alembic.sqlalchemy.org/en/latest/tutorial.html>) для создания миграций для начальной загрузки вашей базы данных, а затем дополнительную миграцию с добавлением необязательного поля «скорость» в модель космического корабля.

# День 07
## Упражнение 00: Пенсионный план
Вы должны разработать свою собственную версию [теста Войта-Кампфа](<https://bladerunner.fandom.com/wiki/Voight-Kampff_test>). Для этого следует подготовить набор вопросов (достаточно не менее 10) с тремя-четырьмя вариантами ответа на случайный выбор. Эти вопросы и ответы следует хранить в отдельном файле любого формата (например, SQLite или просто JSON).

После каждого ответа человек, задающий вопросы, должен вручную ввести набор переменных:

- Дыхание (измеряется в ударах в минуту, обычно около 12-16 вдохов в минуту)
- Частота сердечных сокращений (обычно от 60 до 100 ударов в минуту)
- Уровень покраснения (категориальный, 6 возможных уровней)
- Расширение зрачка (текущий размер зрачка от 2 до 8 мм)

После десяти вопросов и переменных измерений тест должен вывести строгое бинарное решение о том, является ли отвечающий субъект человеком или репликантом. В этом упражнении вы можете придумать собственную логику для принятия этого решения.

Попробуйте разбить бизнес-логику на отдельные файлы в зависимости от задач, которые решают компоненты. Стартовый скрипт должен называться *main.py*. Все взаимодействие с тестом должно осуществляться через командную строку.

## Упражнение 01: Человеческая жизнь
Нужно написать тесты, чтобы покрыть все возможные положительные и отрицательные случаи.

Охватить тестами все крайние случаи для всех компонентов. В принципе, всякий раз, когда оператор теста вводит что-то неправильное (например, выбирая несуществующий ответ или выходящие за пределы допустимого значения для измерений, например, отрицательную частоту сердечных сокращений), он или она должен получать осмысленное информационное сообщение и возможность повторить ввод.

Рекомендуется использовать фреймворк [Pytest](<https://realpython.com/pytest-python-testing/>). Все тесты должны быть внутри `tests` каталога.

## Упражнение 02: На будущее
Вам необходимо использовать проект [Sphinx](<https://www.sphinx-doc.org/en/master/tutorial/index.html>) для автоматического создания документации для вашего кода, написанного на EX00/EX01.
Полученная документация должна состоять как минимум из двух частей:

- Quickstart, который представляет собой описание того, как работать с тестом (Markdown или RST)
- [Автоматически сгенерированная](<https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html>) ссылка на код, нужно будет добавить [комментарии](<https://realpython.com/documenting-python-code/>)

Вы также должны добавить правильное название и логотип к вашему проекту для документации. Тем не менее, не включайте сгенерированные документы в свою отправку, они должны быть созданы `make html` на стороне вашего коллеги, если установлены все требования.

# День 08
## Упражнение 00: Я знаю кунг-фу
Для Нео и Агента доступны только 4 действия:
```
class Action(Enum):
    HIGHKICK = auto()
    LOWKICK = auto()
    HIGHBLOCK = auto()
    LOWBLOCK = auto()
```
Рецепт победы в бою прост: для каждого удара Нео должен защищать ту часть (высокую/низкую), куда целится агент, и для каждого блока он должен целиться в незаблокированную часть тела.

Написать скрипт под названием `«fight.py»`, который будет включать в себя асинхронную функцию «fight()» и для бонуса «fightmany(n)» (где вместо одного агента Нео будет сражаться с несколькими (списком) из них)

## Упражнение 01: Кальмар на палочке
Программа должна состоять из двух файлов - `crawl.py` и `server.py`. Рекомендуется использовать [aiohttp](<https://docs.aiohttp.org/en/stable/>) или [httpx](<https://www.python-httpx.org/>) для клиентской части и [FastAPI](<https://fastapi.tiangolo.com/>) для серверной. Весь код ввода-вывода должен быть асинхронным.

## Упражнение 02: Дежавю
Вы должны использовать Redis как для кэша, так и для счетчиков домена. Весь код по-прежнему должен быть асинхронным и использовать парадигму async/await. Вы можете рассмотреть возможность использования библиотеки [aioredis](<https://aioredis.readthedocs.io/en/latest/>) для этой задачи. Поскольку код клиента не затрагивается, вы должны отправить только один файл с измененным кодом сервера EX01 под названием «server_cached.py».

# День 09
## Упражнение 00: все еще считается
Написать простой модуль калькулятора для Python (используя Python C API) с четырьмя функциями:
- add(a, b)
- sub(a, b)
- mul(a, b)
- div(a, b)

Этот модуль должен состоять из двух файлов — «calculator.c» и «setup.py» для его сборки. Код должен правильно обрабатывать ошибки деления на ноль, вызывая встроенное исключение Python из кода C. Модуль должен включать только два файла, и его можно установить с помощью `python setup.py install`. В качестве бонуса добавить обработку double.

## Упражнение 01. Доля секунды
Вам нужно использовать встроенную `ctypes` библиотеку Python для реализации интерфейса монотонных часов в вашей операционной системе. Windows, Linux и MacOS имеют эту функцию как часть стандартной библиотеки. Python [тоже есть сейчас](<https://peps.python.org/pep-0418/#time-monotonic>), но вам следует написать свою версию с нуля.

Это должна быть вызываемая функция `monotonic()` в файле `monotonic.py`, а возвращаемое значение должно быть в секундах (некоторые ОС также поддерживают наносекунды).

## Упражнение 02: Автопилот
На этот раз вам нужно использовать третий способ ускорения вычислений в Python — [Cython](<https://cython.org/>). Мы не углубляемся в науку о данных, но [умножение матриц](<https://en.wikipedia.org/wiki/Matrix_multiplication>) — довольно простая и понятная процедура.

Вы должны написать свою собственную функцию `mul()` на Cython (имя файла `multiply.pyx`) и (как в EX00) реализовать соответствующий `setup.py` файл для создания пакета Python с именем «matrix».

Код должен работать только с целыми числами. Не используйте встроенную реализацию из [Numpy](<https://numpy.org/>) для этой задачи. Дополнительно напишите тест производительности в файле `test_mul_perf.py`, сравнивающий базовую реализацию на чистом Python с вашей на Cython.


## Задания КФУ
#### **Часть 1.** 
Написать консольную программу, которая принимает IP и возвращает страну, с
помощью API https://ip-api.com/docs/api:json

Если IP не существует, нужно вывести ошибку "Такого IP не существует".

Инструкция: При выполнении задания воспользуйтесь библиотекой requests, обратите внимание на статус ĸоды, которые возвращает API.

**Часть 2.** 
Написать консольную программу, которая выводит погоду с сайта
https://yandex.ru/pogoda на сегодня и на неделю.

Инструкция: Для выполнения задания нужно разбирать содержимое HTML и извлекать оттуда нужную информацию. Понять, что ĸонĸретно нужно вытащить из страницы, помогут инструменты разработчика в браузере. Они вызываются с помощью клавиш
*CTRL+SHIFT+I* на Windows и Linux и *CMD+ALT+I* на MacOS.

## Полезное
Многие операции уже представлены в виде методов в стандартной библиотеке, например, для строк вы можно обратиться [по этой ссылке](<https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str>).

Модуль [Python Argparse](<https://docs.python.org/3/howto/argparse.html>) для разбора аргументов командной строки. 

[Подсказки типов](<https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html>), краткая памятка, показывающая, как использовать аннотации типов для различных распространенных типов в Python

Также рекомендуется написать несколько тестов для различных случаев внутри ваших скриптов. Чтобы заставить их работать только тогда, когда скрипт выполняется напрямую, а не импортируется откуда-то еще, вы можете использовать if __name__ == \"__main__\":оператор. [Подробнее](<https://www.geeksforgeeks.org/what-does-the-if-__name__-__main__-do/>)

Небольшой [учебник](<https://ncase.me/trust/>) по теории игр

В Python есть несколько неизменяемых типов объектов. например, [замороженные наборы](<https://docs.python.org/3/library/stdtypes.html#frozenset>).

Python имеет встроенный способ изменения поведения функций без прямого изменения их кода. Он называется a [decorator](<https://realpython.com/primer-on-python-decorators/>) и представляет собой просто специальный синтаксис для функции, которая принимает функцию в качестве аргумента и возвращает функцию. 

[Pytest](<https://realpython.com/pytest-python-testing/>), [теста Войта-Кампфа](<https://bladerunner.fandom.com/wiki/Voight-Kampff_test>)

[Sphinx](<https://www.sphinx-doc.org/en/master/tutorial/index.html>) для автоматического создания документации. [Написание строк документации](<https://realpython.com/documenting-python-code/>)

В синхронном мире люди часто реализуют это с помощью таких модулей, как [Celery](<https://docs.celeryq.dev/en/stable/getting-started/introduction.html>).

[Парадигма async/await](<https://docs.python.org/3/library/asyncio-task.html>).
 