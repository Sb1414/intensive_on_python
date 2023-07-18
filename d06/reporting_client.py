#!/usr/bin/env python3

import sys
import grpc
import reporting_pb2
import reporting_pb2_grpc


def run_client(coordinates):
    channel = grpc.insecure_channel('localhost:50051') # создается канал связи с сервером, незащищенное соединение
    stub = reporting_pb2_grpc.ReportingStub(channel) # экземпляр клиентского stub на основе сгенерированного класса
    coordinates_str = ' '.join(coordinates)  # преобразование в строку координат из командной строки
    request = reporting_pb2.Coordinates(coordinates=coordinates_str)
    # запрос к серверу с использованием метода GetSpaceships stub'а
    spaceships = stub.GetSpaceships(request)
    for spaceship in spaceships: # результаты итерируются и выводятся на экран
        print(spaceship)


if __name__ == '__main__':
    coordinates = sys.argv[1:]
    run_client(coordinates)
