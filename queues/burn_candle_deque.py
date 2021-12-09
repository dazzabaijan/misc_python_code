from threading import Thread
from collections import deque
import time

def burn(direction, next_source):
    while True:
        try:
            next = next_source()
        except IndexError:
            break
        else:
            print(direction, next)
            time.sleep(1)

    print(direction, 'done!')
    
if __name__ == "__main__":
    iterable = range(0, 4)
    candle = deque(iterable)
    
    left = Thread(target=burn, args=('Left', candle.popleft))
    right = Thread(target=burn, args=('Right', candle.pop))
    
    left.start()
    right.start()