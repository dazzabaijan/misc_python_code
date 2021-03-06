from collections import deque

class Queue:
    
    def __init__(self):
        self.buffer = deque()
    
    def enqueue(self, val):
        self.buffer.appendleft(val)
    
    def dequeue(self):
        if len(self.buffer) == 0:
            print("Queue is empty")
            continue
                
        return self.buffer.pop()
    
    def is_empty(self):
        return len(self.buffer) == 0
    
    def size(self):
        return len(self.buffer)
    

if __name__ == "__main__":
    pq = Queue()
    
    pq.enqueue({
        'company': 'Wal Mart',
        'timestamp': '15 apr, 11:01 AM',
        'price': 131.10
    })
    
    pq.enqueue({
        'company': 'Wal Mart',
        'timestamp': '15 apr, 11:02 AM',
        'price': 132
    })
    
    pq.enqueue({
        'company': 'Wal Mart',
        'timestamp': '15 apr, 11:03 AM',
        'price': 135
    })
    
    pq.buffer # shows all elements
    
    pq.dequeue() # gives the first price at 11:01 AM because FIFO