from queue import  BiQueue

q = BiQueue()
q.enqueue("A", 5)
q.enqueue("B", 1)
q.enqueue("C", 3)
print(q.dequeue('oldest'))
print(q.dequeue('newest'))
print(q.queue)