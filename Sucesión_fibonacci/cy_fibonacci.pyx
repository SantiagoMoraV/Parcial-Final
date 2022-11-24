#cython: language level=3
cimport cython

"""
Fecha: 22 Nov 2022
Autor: Santiago Mora
Algoritmo de la sucesión de Fibonacci

"""

cpdef int fibonacci(int n):
    if n < 2:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
