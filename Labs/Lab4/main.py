from queue import  BiQueue

q = BiQueue()
q.enqueue("A", 5)
q.enqueue("B", 1)
q.enqueue("C", 3)
print(q.dequeue('highest'))
print(q.dequeue('lowest'))
print(q.queue)