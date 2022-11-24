import time
import py_areaTria
import cy_areaTria
import random


b=random.randint(0,100000)
h=random.randint(0,100000)
ladc=random.randint(0,100000)
apt=random.randint(0,100000)
numlad=random.uniform(0,100000)
lonlad=random.uniform(0,100000)
porc=random.randint(0,100000)
num=random.randint(0,100000)


init_time=time.time()



time_spam = 400
n_steps=2000000


formato_datos = "{:.5f},{:5f}\n"
for i in range(30):
	iniciopy = time.time()
	py_areaTria.single_step(b, h, ladc, apt, numlad, lonlad, porc, num)
	finalpy=time.time() - iniciopy
	
	iniciocy = time.time()
	cy_areaTria.single_step(b, h, ladc, apt, numlad, lonlad, porc, num)
	finalcy=time.time() - iniciocy
		
	with open("Resultados.csv","a") as archivo:
		archivo.write(formato_datos.format(finalpy,finalcy))
	
	
	
