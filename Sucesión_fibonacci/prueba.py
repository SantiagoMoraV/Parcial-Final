import timeit
import cy_fibonacci.pyx

py = timeit.timeit("fibonacci(30)", "from __main__ import fibonacci", number=30)

cy = timeit.timeit("fibonacci(30)", "from cy_fibonacci import py_fibonacci", number=30)

