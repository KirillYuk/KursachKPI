from queue import BiQueue

print("TESTS")


q = BiQueue()
q.enqueue("A", 5)
q.enqueue("B", 1)
q.enqueue("C", 3)

print("dequeue highest:", "PASS" if q.dequeue('highest') == "A" else "FAIL")
print("dequeue lowest:", "PASS" if q.dequeue('lowest') == "B" else "FAIL")


q = BiQueue()
q.enqueue("A", 5)
q.enqueue("B", 1)
q.enqueue("C", 3)

print("dequeue oldest:", "PASS" if q.dequeue('oldest') == "A" else "FAIL")
print("dequeue newest:", "PASS" if q.dequeue('newest') == "C" else "FAIL")


q = BiQueue()
q.enqueue("A", 5)
q.enqueue("B", 1)
q.enqueue("C", 3)

print("peek highest:", "PASS" if q.peek('highest') == "A" and len(q.queue) == 3 else "FAIL")
print("peek lowest:", "PASS" if q.peek('lowest') == "B" and len(q.queue) == 3 else "FAIL")
print("peek oldest:", "PASS" if q.peek('oldest') == "A" and len(q.queue) == 3 else "FAIL")
print("peek newest:", "PASS" if q.peek('newest') == "C" and len(q.queue) == 3 else "FAIL")


q = BiQueue()

print("empty queue: PASS" if q.dequeue('highest') is None else "FAIL")
