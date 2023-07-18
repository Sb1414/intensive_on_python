import random
import grpc
from concurrent import futures
import reporting_pb2
import reporting_pb2_grpc


# реализация серверной службы на основе сгенерированного класса
class ReportingServicer(reporting_pb2_grpc.ReportingServicer):
    # обрабатывает запрос от клиента и возвращает объекты Spaceship через итератор yield
    def GetSpaceships(self, request, context):
        coordinates = request.coordinates
        num_spaceships = random.randint(1, 10)
        for _ in range(num_spaceships):
            spaceship = generate_spaceship()
            yield spaceship


def generate_spaceship():
    # создает случайный объект Spaceship с заполненными случайными значениями
    spaceship = reporting_pb2.Spaceship()
    # случайное значение для поля alignment объекта Spaceship. Выбирается случайным образом из списка
    # [reporting_pb2.Ally, reporting_pb2.Enemy].
    # reporting_pb2.Ally и reporting_pb2.Enemy представляют значения перечисления Alignment из файла .proto
    spaceship.alignment = random.choice([reporting_pb2.Ally, reporting_pb2.Enemy])
    # случайное имя для корабля, которое представляет собой строку "Spaceship" с добавленным случайным числом от 1 до 100
    spaceship.name = "Spaceship " + str(random.randint(1, 100))
    # случайное значение для поля classification объекта Spaceship. Оно выбирается случайным образом из списка [reporting_pb2.Corvette, reporting_pb2.Dreadnought]
    # reporting_pb2.Corvette и reporting_pb2.Dreadnought представляют значения перечисления Class из файла .proto
    spaceship.classification = random.choice([reporting_pb2.Corvette, reporting_pb2.Dreadnought])
    # устанавливается случайное значение для поля length, которое представляет длину корабля. Случайное число в диапазоне от 100.0 до 20000.0 с помощью функции random.uniform()
    spaceship.length = random.uniform(100.0, 20000.0)
    # случайное значение для поля crew_size, которое представляет размер экипажа корабля. Случайное число выбирается в диапазоне от 0 до 10 с помощью функции random.randint()
    spaceship.crew_size = random.randint(0, 10)
    # случайное значение для поля armed, которое указывает, вооружен ли корабль. Значение выбирается случайным образом из списка [True, False] с помощью функции random.choice()
    spaceship.armed = random.choice([True, False])
    # проверяется, если размер экипажа crew_size больше 0, то добавляется офицер в список officers
    if spaceship.crew_size > 0:
        # Создается новый объект Officer, и ему присваиваются значения для полей first_name, last_name и rank
        officer = spaceship.officers.add()
        officer.first_name = "First"
        officer.last_name = "Officer"
        officer.rank = "Captain"
    # возвращает сгенерированный объект Spaceship
    return spaceship


def serve():
    # создается сервер gRPC с использованием grpc.server и
    # futures.ThreadPoolExecutor для обработки запросов в отдельных потоках
    server = grpc.server(futures.ThreadPoolExecutor())
    reporting_pb2_grpc.add_ReportingServicer_to_server(ReportingServicer(), server) # добавляется экземпляр ReportingServicer к серверу
    server.add_insecure_port('[::]:50051') # устанавливается незащищенный порт для прослушивания входящих соединений
    # Сервер запускается с помощью start и ожидает завершения работы с помощью wait_for_termination
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()

# клиент отправляет запрос с координатами на сервер, который возвращает случайные объекты Spaceship
# через потоковый ответ. Клиент получает эти объекты и выводит их на экран