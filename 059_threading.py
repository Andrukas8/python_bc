# thread - flow of running. We can have program run in multiple flows.

import threading
import time


def eat_breakfast():
    time.sleep(3)
    print("You eat breakfast")


def drink_coffee():
    time.sleep(4)
    print("You drank coffee")


def study():
    time.sleep(5)
    print("You finish studying")


x = threading.Thread(target=eat_breakfast, args=())
x.start()

y = threading.Thread(target=drink_coffee, args=())
y.start()

z = threading.Thread(target=study, args=())
z.start()

x.join()  # main thread has to wait for x before it can go on wit the rest of its instructions
y.join()
z.join()


print(threading.active_count())
print(threading.enumerate())
print(time.perf_counter())
