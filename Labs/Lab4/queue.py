class BiQueue:
    def __init__(self):
        self.queue = []
        self.counter = 0
    
    def enqueue(self, item, priority):
        self.queue.append((self.counter, priority,item))
        self.counter +=1