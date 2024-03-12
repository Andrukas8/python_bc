# Multiprocessing - running tasks in parallel on different cpu cores, bypass GIL used for threads
# multiprocessing - better for cpu bound tasks (heavy cpu usage)
# multithreading - better for io bound tasks (waiting around)

from multiprocessing import Process, cpu_count
import time


def counter(num):
    count = 0
    while count < num:
        count += 1


def main():
    print(cpu_count())
    a = Process(target=counter, args=(125_000_000,))
    b = Process(target=counter, args=(125_000_000,))
    c = Process(target=counter, args=(125_000_000,))
    d = Process(target=counter, args=(125_000_000,))
    e = Process(target=counter, args=(125_000_000,))
    f = Process(target=counter, args=(125_000_000,))
    g = Process(target=counter, args=(125_000_000,))
    h = Process(target=counter, args=(125_000_000,))

    a.start()
    b.start()
    c.start()
    d.start()
    e.start()
    f.start()
    g.start()
    h.start()
    
    a.join()
    b.join()
    c.join()
    d.join()
    e.join()
    f.join()
    g.join()
    h.join()
    
    print(f"Finished in {time.perf_counter()} seconds")

if __name__ == '__main__':
    main()