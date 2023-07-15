import random
import time

def emit_gel(pressure, step):
    while True:
        pressure += random.uniform(0, step)
        if pressure > 100:
            raise ValueError(f"Pressure too high: {pressure}")
        yield pressure

def valve():
    step_sign = 20  # шаг
    pressure = 75  # начальное давление
    generator = emit_gel(pressure, step_sign)  # значение шага
    while True:
        try:
            pressure = next(generator)
            if pressure < 10:
                print(f"Pressure too low: {round(pressure)}")
                break
            elif pressure > 90:
                print(f"Pressure too high: {round(pressure)}")
                break
            elif pressure < 20 or pressure > 80:
                step_sign *= -1  # изменение направления
                generator = emit_gel(pressure, step_sign)  # новый генератор с обновленным давлением и знаком остановки
            print(f"Pressure: {round(pressure)}")
            time.sleep(0.5)  # задержка между измерениями давления
        except ValueError as e:
            print(e)
            break
        except StopIteration:
            break

if __name__ == "__main__":
    valve()
