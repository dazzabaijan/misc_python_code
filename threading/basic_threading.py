import time
import threading
import concurrent.futures

start = time.perf_counter()

def do_something(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    return f'Done Sleeping...{seconds}'


"""Create and join threads using Thread Pool Executor"""
with concurrent.futures.ThreadPoolExecutor() as executor:
    secs = [5, 4, 3, 2, 1]
    results = executor.map(do_something, secs)
    
    for result in results:
        print(result)

"""Create and join multiple threads"""

threads = []

for _ in range(10):
    t = threading.Thread(target=do_something, args=[1.5])
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()
    
"""Create and join threads individually"""

# create threads
thread_1 = threading.Thread(do_something)
thread_2 = threading.Thread(do_something)

# use start method to run our threads
thread_1.start()
thread_2.start()

# use join method to make sure they complete before moving on to calculating finish time
thread_1.join()
thread_2.join()

finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} second(s)')