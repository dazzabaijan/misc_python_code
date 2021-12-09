from collections import deque

class Queue():
    
    def __init__(self) -> None:
        self.buffer = deque()
        
    def enqueue(self, value) -> None:
        self.buffer.appendleft(value)
        
    def dequeue(self):
        if len(self.buffer) == 0:
            print("Queue is empty")
            pass
        
        return self.buffer.pop()
    
    def is_empty(self):
        return len(self.buffer) == 0
    
    def size(self):
        return len(self.buffer)
    
    def front(self):
        return self.buffer[-1]
    
def print_binary_numbers(n):
    numbers_queue = Queue()
    numbers_queue.enqueue("1")
    
    for i in range(n):
        front = numbers_queue.front()
        print(front)
        numbers_queue.enqueue(front + "0")
        numbers_queue.enqueue(front + "1")
        
        numbers_queue.dequeue()
        
if __name__ == "__main__":
    print_binary_numbers(10)
    
        