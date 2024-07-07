def factorial(x):
    if(x == 1):
        return x
    return x * factorial(x-1)
result = factorial(6)
print(result)