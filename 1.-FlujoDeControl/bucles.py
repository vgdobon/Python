n = int(input("Dime un numero: "))

while n != 1:
    print(n, end=", ")
    if n % 2 == 0:  # par
        n = n // 2
    else:
        n = n * 3 + 1
print(n, end=".\n")