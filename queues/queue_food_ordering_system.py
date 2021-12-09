from collections import deque
from threading import Thread
import time

class Queue():
    
    def __init__(self):
        self.buffer = deque()
        
    def enqueue(self, value):
        self.buffer.appendleft(value)
        
    def dequeue(self):
        if len(self.buffer) == 0:
            print("Queue is empty")
            raise Exception("Queue is empty")
        
        return self.buffer.pop()
    
    def is_empty(self):
        return len(self.buffer) == 0
    
    def size(self):
        return len(self.buffer)

def place_orders(queue, orders):
    
    for order in orders:
        time.sleep(0.5)
        queue.enqueue(order)


def serve_orders():
    
    time.sleep(1)
    while True:
        if food_order_queue.is_empty():
            break
        
        order = food_order_queue.dequeue()
        print(f"Now serving: {order}")
        time.sleep(2)
        

if __name__ == "__main__":
    orders = ['pizza', 'samosa', 'pasta', 'biryani', 'burger']
    
    food_order_queue = Queue()
    t1 = Thread(target=place_orders, args=(food_order_queue, orders,))
    t2 = Thread(target=serve_orders)
    
    t1.start()
    t2.start()
    