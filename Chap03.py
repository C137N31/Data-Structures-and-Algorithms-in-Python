#R3.1

import matplotlib.pyplot as plt
import numpy
import math

x = [10**i for i in range(10)]

funcs = [lambda x: 8*x,
         lambda x: 4*x*math.log(x),
         lambda x: 2*x**2,
         lambda x: x**3
         #lambda x: 2**x
        ]

ys = []

for func in funcs:
    ys.append(list(map(func, x)))

for y in ys:
    plt.plot(x,y)
plt.yscale('log')
plt.xscale('log')
plt.show()         
