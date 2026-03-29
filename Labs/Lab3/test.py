import time
from mem import memo

@memo(ttl=2)
def multiply(x, y=2):
    print("calc", x, "*", y)
    return x * y

print(multiply(2))
print(multiply(2))
time.sleep(2)
print(multiply(2))
print(multiply(2))
time.sleep(1.99)
print(multiply(2))