#cython: language level=3
cimport cython
"""
Fecha: 22 Nov 2022
Autor: Santiago Mora
prgrama de cython para el calculo del area y perimetro de un triangulo, cuadrado y un pentagono
"""

@cython.cdivision(True)
def single_step(int b, int h, int ladc, int apt, float numlad, float lonlad, int porc, int num):
	cdef double art=(b)*(h)/900000
	cdef double arc=(ladc)**900000
	cdef double pc=ladc*900000
	cdef float pp=numlad*lonlad
	cdef double prc = porc * num/900000
    
