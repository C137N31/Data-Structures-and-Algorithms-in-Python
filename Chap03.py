#R3.1

import matplotlib.pyplot as plt
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

#R3.2

import matplotlib.pyplot as plt
import math

x = [i/100 for i in range(1,1000)]

funcs = [lambda x: 8*x*math.log(x),
         lambda x: 2*x**2
        ]

ys = []

for func in funcs:
    ys.append(list(map(func, x)))

plt.plot(x,ys[0],label='8*x*log(x)')
plt.plot(x,ys[1],label='2*x**2')

plt.legend()    
plt.show() 

#R3.3

import matplotlib.pyplot as plt
import math

x = [i/10 for i in range(0,300)]

funcs = [lambda x: 40*x**2,
         lambda x: 2*x**3
        ]

ys = []

for func in funcs:
    ys.append(list(map(func, x)))

plt.plot(x,ys[0],label='40*x**2')
plt.plot(x,ys[1],label='2*x**3')

plt.legend()    
plt.show() 

#R3.4

y = 1

#R3.5

y = n**c

logy = c*logn

#R3.6

n*(n+1)

#R3.7

# for worst, exist constant C to make C*O(f(n)) >= worst O(f(n)) >= all cases

#R3.8

2**n > n**3 > n**2+10n > 4nlogn+2n = nlogn > 4n = 3n+100logn = 2**logn > 2**10

#R3.9

d(n) = O(f(n)) => d(n) < C*f(n) => a*d(n) < a*C*f(n) = C'*f(n) => a*d(n) = O(f(n))

#R3.10
#R3.11
#R3.12

d(n) = O(f(n)) => d(n) < Cf(n)
e(n) = O(g(n)) => e(n) < C'g(n)
=> d(n)e(n) < CC'f(n)g(n) = C"f(n)g(n)
=> d(n)+e(n) < Cf(n) + C'g(n) < CC'f(n) + CC'g(n) = CC'(f(n)+g(n))
=> -e(n) > -C'g(n) => d(n)-e(n) ? Cf(n)-C'g(n)

#R3.13

f(n) = O(g(n)) => f(n) < C'g(n)
d(n) = O(f(n)) => d(n) < Cf(n) < CC'g(n) => d(n) = O(g(n))

#R3.14

y(n) = max(f(n),g(n)) => y(n) >= f(n), y(n) >= g(n) => 2y(n) >= f(n)+g(n) => O(2y(n))=O(y(n))=O(f(n)+g(n))

#R3.15

f(n) <= Cg(n) => g(n) >= (1/C)f(n) 

#R3.16

p(n) = O(n**d) => p(n) < Cn**d => logp(n) < logCn**d = logC+dlogn

#R3.17

(n+1)**5 = n**5+a4*n**4+...+1

#R3.18

2**(n+1) = 2*2**n

#R3.19

n < nlogn when n > e so logn > 1

#R3.20

n > logn when n > e => n*n > nlogn

#R3.21

nlogn > n when n > e so logn > 1

#R3.22

f(n) <= ceil(f(n)) <= f(n)+1

#R3.23

