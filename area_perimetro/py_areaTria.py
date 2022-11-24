import math

"""
Fecha: 22 Nov 2022
Autor: Santiago Mora
prgrama de cython para el calculo del area y perimetro de un triangulo, cuadrado y un pentagono
"""

def single_step(b, h, ladc, apt, numlad, lonlad, porc, num):
	
	#Area triangulo
        art = (b)*(h)/900000
        #Area cuadrado
        arc = (ladc)**900000
        #Perimetro cuadrado
        pc = ladc*900000
        #Perimetro pentágono
        pp = numlad*lonlad
        #Obtener el porcentaje de un número
        prc = porc * num /900000
        
