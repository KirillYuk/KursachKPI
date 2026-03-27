from mem import memo

@memo()
def multiply(x, y=1):
    print("calc", x, "*", y)
    return x * y

print(multiply(3))
print(multiply(3))
print(multiply(5))
print(multiply(5))
print(multiply(5, 3))
print(multiply(5, 3))
print(multiply(6, 4))
print(multiply(6, y=4))
print(multiply(x=6, y=4))