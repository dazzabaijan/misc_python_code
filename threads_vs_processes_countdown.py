import time
from threading import Thread
from multiprocessing import Pool

COUNT = 50000000

def countdown(n):
    while n > 0:
        n -= 1

if __name__ == '__main__':

    t1 = Thread(target=countdown, args=(COUNT//2,))
    t2 = Thread(target=countdown, args=(COUNT//2,))

    start = time.perf_counter()
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    end = time.perf_counter()

    print(f'Multithreading time taken {end - start} seconds')

    pool = Pool(processes=2)
    start = time.perf_counter()
    r1 = pool.apply_async(countdown, [COUNT//2])
    r2 = pool.apply_async(countdown, [COUNT//2])
    pool.close()
    pool.join()
    end = time.perf_counter()

    print(f'Multiprocessing time taken {end - start} seconds')
    