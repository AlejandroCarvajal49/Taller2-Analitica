def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(10)) 

def proporcion_aurea(n):
    phi = (1 + 5 ** 0.5) / 2
    return round(phi ** n / 5 ** 0.5)

print(proporcion_aurea(10))  

def numero_par(n):
    return n % 2 == 0

def numero_impar(n):
    return n % 2 != 0

def numero_fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

    print("Hola")
