def factorial(n):
    if n == 0:
        # Define our base (trivial) case
        return 1
    else:
        return n * factorial(n - 1)
    
print(factorial(5))