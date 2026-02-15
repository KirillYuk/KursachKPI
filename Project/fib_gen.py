import time
a = 0
b = 1

while True:
    print(a)
    temp = a
    a = b
    b = temp + a
    time.sleep(0.5)