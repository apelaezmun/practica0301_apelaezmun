'''
Escribir dos funciones, una función que reciba un número entero positivo n y 
calcule el número de fibonacci asociado a ese número de manera recursiva y 
otra función que haga la misma operación pero con bucles.
Con ambas funciones, calcular y comparar el tiempo de ejecución para 
n = (1, 10, 20, 30 y 40) por fuerza bruta.
'''
import datetime

def fibonacci_recur(n):
    if n <= 1:
        return n
    return fibonacci_recur(n - 1) + fibonacci_recur(n - 2)

def fibonacci_bucle(n):
    a, b = 0, 1
    for _ in range( n + 1):
        a, b = b, a + b
    return b

numeros = [1, 10, 20, 30, 40]

for n in numeros:
    inicio_r = datetime.datetime.now()
    numero_r = fibonacci_recur(n)
    fin_r = datetime.datetime.now()
    tiempo_r = (fin_r - inicio_r)

    inicio_b = datetime.datetime.now()
    numero_b = fibonacci_recur(n)
    fin_b = datetime.datetime.now()
    tiempo_b = (fin_b - inicio_b)
    print('n =', n)
    print('Recursivo:\nResultado =', tiempo_r)
    print('Bucle:\nResultado =', tiempo_b)