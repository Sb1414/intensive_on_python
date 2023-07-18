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
    spaceship.alignment = random.choice([reporting_pb2.Ally, reporting_pb2.Enemy])
    spaceship.name = "Spaceship " + str(random.randint(1, 100))
    spaceship.classification = random.choice([reporting_pb2.Corvette, reporting_pb2.Dreadnought])
    spaceship.length = random.uniform(100.0, 20000.0)
    spaceship.crew_size = random.randint(0, 10)
    spaceship.armed = random.choice([True, False])
    if spaceship.crew_size > 0:
        officer = spaceship.officers.add()
        officer.first_name = "First"
        officer.last_name = "Officer"
        officer.rank = "Captain"
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