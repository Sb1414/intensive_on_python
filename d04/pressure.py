import random
import time
from colorama import Fore, Style

def emit_gel(pressure, step):
    while True:
        pressure += random.uniform(0, step)
        if pressure > 100:
            print(f"{Fore.RED}Pressure too high: {round(pressure)}{Style.RESET_ALL}")
        yield pressure

def valve():
    step_sign = 20  # шаг
    pressure = 50  # начальное давление
    generator = emit_gel(pressure, step_sign)  # значение шага
    while True:
        try:
            pressure = next(generator)
            if pressure < 10:
                print(f"{Fore.RED}Pressure too low: {round(pressure)}{Style.RESET_ALL}")
                break
            elif pressure > 90:
                print(f"{Fore.RED}Pressure too high: {round(pressure)}{Style.RESET_ALL}")
                break
            elif pressure < 20:
                step_sign = abs(step_sign)  # изменение направления на положительное
                generator = emit_gel(pressure, step_sign)  # новый генератор с обновленным давлением и знаком остановки
                print(f"{Fore.YELLOW}Pressure: {round(pressure)}{Style.RESET_ALL}")
            elif pressure > 80:
                step_sign = -abs(step_sign)  # изменение направления на отрицательное
                generator = emit_gel(pressure, step_sign)  # новый генератор с обновленным давлением и знаком остановки
                print(f"{Fore.YELLOW}Pressure: {round(pressure)}{Style.RESET_ALL}")
            else:
                print(f"Pressure: {round(pressure)}")
            time.sleep(0.5)  # задержка между измерениями давления
        except ValueError as e:
            print(e)
            break
        except StopIteration:
            break

if __name__ == "__main__":
    valve()
