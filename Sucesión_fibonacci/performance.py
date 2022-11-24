import time
import py_fibonacci
import cy_fibonacci
import random

#n=random.randint(0,100)
n=33

time_spam = 400
n_steps=2000000


formato_datos = "{:.5f},{:5f}\n"
for i in range(30):
	iniciopy = time.time()
	py_fibonacci.fibonacci(n)
	finalpy=time.time() - iniciopy
	
	iniciocy = time.time()
	cy_fibonacci.fibonacci(n)
	finalcy=time.time() - iniciocy
	with open("fibonacci.csv","a") as archivo:
		archivo.write(formato_datos.format(finalpy,finalcy))
