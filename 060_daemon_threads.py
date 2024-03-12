# daemon thread - is a thread that runs in the background, not important for the program to run your program
# non-daemon thread can't be stopped until their task is complete


import threading
import time


def timer():
    print()
    count = 0
    while True:
        time.sleep(1)
        count += 1
        print(f"Logged in for {count} seconds")


x = threading.Thread(target=timer, daemon=True)
x.start()

# x.setDaemon(True) # changing a thread to daemon
# x.isDaemon() # check if thread is daemon or not

answer = input("Do you wish to exit?: ")
