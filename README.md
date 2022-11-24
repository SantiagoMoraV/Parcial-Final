# Parcial-Final
## En el actual repositorio, podrá encontrar un par de algoritmos en lenguaje Python y Cython, su propósito es medir el rendimiento de cada lenguaje midiendo los tiempos de ejecucion de cada uno. 

Básicamente en las carpetas, podrán encontrar dos programas que ejecutan una serie de algoritmos sin mucha importancia, la estructura general del programa es un archivo inicial en lenguaje pythno que es el que va a tener el algoritmo inicial, con ese código en Python, se procede a cambiarlo a cython, es decir con lo agregado de c, esa es la estructura básica. Sin embargo, no hay que dejar de lado el archivo performance, este archivo se encarga de ejecutar en bucle el programa y almacenar los tiempos de ejecución de cada lenguaje en un archivo.csv para luego poder analizar dichos datos de manera más sencilla. 

Luego como compilador de todo esto tenemos el archivo setup, que lo que hace es crear un archivo .c que simula el código de Python, luego tenemos el Makefile que es el que nos permite unificar todo el proceso y aparte nos da la posibilidad de borrar el archivo .c y el objeto.

Para ejecutar dichos programas en la terminal de ubuntu, se debe acceder a la ubicacion desde la terminal hasta la carpeta donde reposan todos los codigos anteriormente mencionados, usaremos un make all, para verificar que el codigo no tenga errores y permita compilar, para despues hacer la prubea y generar el .csv invocando al "perfomance" ingresando "phyton3 perfomance.py" una vez que el make all haya pasado sin inconvenientes.
