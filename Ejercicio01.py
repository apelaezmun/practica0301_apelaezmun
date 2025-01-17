'''
Escribir dos funciones, una función que reciba un número entero positivo n y 
calcule el número de fibonacci asociado a ese número de manera recursiva y 
otra función que haga la misma operación pero con bucles.
Con ambas funciones, calcular y comparar el tiempo de ejecución para 
n = (1, 10, 20, 30 y 40) por fuerza bruta.
'''
import datetime
def fibonacci_recursivo(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci_recursivo(n-1) + fibonacci_recursivo(n - 2)
    

a, b = 0, 1
def fibonacci_bucle(n):
    if n <= 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    for i in range(2, n):
        a, b = b, a + b
        return b

n = [1, 10, 20, 30, 40]
print(fibonacci_recursivo(n))
print(fibonacci_bucle(n))