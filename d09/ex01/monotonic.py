import ctypes
import os
import time
import platform

def monotonic():
    system = platform.system()
    if system == "Windows":
        winmm = ctypes.windll.winmm
        return winmm.timeGetTime() / 1000.0
    elif system == "Linux":
        libc = ctypes.CDLL("libc.so.6")
        timespec = ctypes.c_longlong()
        libc.clock_gettime(1, ctypes.byref(timespec))
        return timespec.value / 1e9
    elif system == "Darwin":
        libSystem = ctypes.CDLL("/usr/lib/libSystem.dylib")
        time = ctypes.c_longlong()
        libSystem.clock_gettime(0, ctypes.byref(time))
        return time.value / 1e9
    else:
        raise NotImplementedError("тру парни вообще-то используют винду, линукс или макос")


if __name__ == '__main__':
    print(monotonic())
    time.sleep(1)
    print(monotonic())
