import time

def fib_gen():
    a = 0
    b = 1
    while True:
        yield a
        next_val = a + b
        a = b
        b = next_val

for val in fib_gen():
    print(val)
    time.sleep(0.5)