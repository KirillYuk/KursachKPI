from mem import memo

@memo()
def multiply(x):
    print("calc for", x)
    return x*x

print(multiply(3))
print(multiply(3))
print(multiply(5))
print(multiply(5))
print(multiply(5))