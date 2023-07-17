import threading
import time
import random

class Doctor(threading.Thread):
    def __init__(self, number, left_screwdriver, right_screwdriver):
        threading.Thread.__init__(self)
        self.number = number
        self.left_screwdriver = left_screwdriver
        self.right_screwdriver = right_screwdriver

    def run(self):
        self.think()
        self.act()

    def think(self):
        # print("Doctor {}: Ожидание...".format(self.number))
        time.sleep(random.randint(1, 3))

    def act(self):
        # print("Doctor {}: Берет отвертку...".format(self.number))
        self.left_screwdriver.acquire()
        time.sleep(0.1)  # время на захват левой отвертки
        self.right_screwdriver.acquire()

        print("Doctor {}: BLAST!".format(self.number))

        self.right_screwdriver.release()
        self.left_screwdriver.release()

        time.sleep(random.randint(1, 3))

def main():
    random.seed(42)
    screwdrivers = [threading.Semaphore(1) for _ in range(5)]

    doctors = []
    for i in range(5):
        left_screwdriver = screwdrivers[i]
        right_screwdriver = screwdrivers[(i + 1) % 5]
        doctor = Doctor(i + 9, left_screwdriver, right_screwdriver)
        doctors.append(doctor)

    for doctor in doctors:
        doctor.start()

    for doctor in doctors:
        doctor.join()

if __name__ == "__main__":
    main()
