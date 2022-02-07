#R1.1

def is_multiple(n, m):
    if m == 0: return False
    return ( n%m == 0 )

print (is_multiple(3,0))
print (is_multiple(0,0))
print (is_multiple(3,2))
print (is_multiple(4,2))
print (is_multiple(-4,2))

#R1.2

def is_even(n:int):
    assert  type(n) == int, "input integer"
    return ( n&1 == 0 )

print (is_even(2.5))
print (is_even(0))
print (is_even(3))
print (is_even(4))
print (is_even(-4))

#R1.3

def minmax(data):
    minn = maxn= data[0]
    for n in data:
        if minn > n: minn = n
        if maxn < n: maxn = n
    return(minn,maxn)

print (minmax((2,4,9,2,5,5,7)))

#R1.4
#R1.5

def sumsquare(n:int):
    assert type(n) == int, 'input integer'
    if n < 1:
        print('input positive integer')
        return False
       
    return(sum(i*i for i in range(1,n)))

print (sumsquare(9))
print (sumsquare(-1))
print (sumsquare(3.54))

#R1.6
#R1.7

def sumsquare(n:int):
    assert type(n) == int, 'input integer'
    if n < 1:
        print('input positive integer')
        return False
       
    return(sum(i*i for i in range(1,n,2)))

print (sumsquare(9))
print (sumsquare(-1))
print (sumsquare(3.54))

#R1.8
j = n+k

#R1.9
list(range(50,90,10))

#R1.10
list(range(8,-9,-2))

#R1.11
[2**n for n in range(9)]

#R1.12
import random

def randomchoice(data):
    return data[random.randrange(0,len(data))]

data = [1, 3, 4, 6, 9, 2]    
for i in range(3):
    print(randomchoice(data), end=' ')

#C1.13

def reverse(data):
    for i in range(len(data)//2):
        data[i], data[len(data)-i-1] = data[len(data)-i-1], data[i]
    return data

data = [1, 3, 4, 7, 6, 9, 2]    
print(reverse(data))    

#C1.14

def product_odd(data):
    for i in range(len(data)):
        for j in range(i,len(data)):
            if data[i] != data[j] and (data[i]*data[j])&1 == 1:
                yield (data[i], data[j])

data = [1, 3, 4, 7, 6, 9, 2]    
oddpair = product_odd(data)
for op in oddpair:
    print(op)

#C1.15

def all_distinct(data):
    for i in range(len(data)):
        for j in range(i+1,len(data)):
            if data[i] == data[j]:
                return False
    return True

data = [1, 3, 4, 7, 6, 9, 2]    
print(all_distinct(data))
    
#C1.16

# Although numeric types are immutable, lists are mutable. The scale function creates a new object, its reference is stored in the original list structure. 
# The changes in the list are the references to new objects.

#C1.17

def scale(data, factor):
    for val in data:
        val *= factor

def realscale(data, factor):
    for i in range(len(data)):
        data[i] *= factor

data = [1, 3, 4, 7, 6, 9, 2]    
print(data)
scale(data,2)
print(data)
realscale(data,2)
print(data)

[1, 3, 4, 7, 6, 9, 2]
[1, 3, 4, 7, 6, 9, 2]
[2, 6, 8, 14, 12, 18, 4]

# val *= factor creates a new instance of val, but doesn't change the reference to the original object in the list
# data[i] changes the reference to element i, which changes the original array

#C1.18

def gen_list():
    a = 0
    i = 0
    while True:
        yield a
        i += 1
        a += 2*i

list = gen_list()

print([next(list) for _ in range(10)])

#C1.19

# chr(97) = 'a'
[chr(97+i) for i in range(26)]

#C1.20

import random

def shuffle2(data):
    shuffledata = []
    indices = set()
    for i in range(len(data)):
        j = random.randint(0,len(data)-1)
        while j in indices:
            j = random.randint(0,len(data)-1)

        shuffledata.append(data[j])
        indices.add(j)
    
    return shuffledata
    
data = [1, 3, 4, 7, 6, 9, 2]

print(shuffle2(data))

#C1.21

def readfile(filepath):
    file = open(filepath)
    lines = []

    while True:
        try:
            line = file.readline()
            if line == '': raise EOFError
            lines.append(line[:-1])
        except EOFError:
            for line in reversed(lines):
                print(line)
            return

readfile(r'Project/Exercises/Chap01/test.txt')

#C1.22

def dot_product(a,b):
    assert len(a) == len(b), 'Error, lengths must be euqal'
    c = [None]*len(a)

    for i in range(len(a)):
        c[i] = a[i]*b[i]

    return c

a = [1,3,5]
b = [3,5,6]

print(dot_product(a,b))

#C1.23

def index_handle(a, index, value):
    try:
        a[index] = value
    except IndexError:
        print("Don't try buffer overflow attacks in Python!")

a = [1,3,5,4,8]

index_handle(a,9,11)
index_handle(a,2,22)
index_handle(a,-1,33)
index_handle(a,-8,44)

print(a)

#C1.24

def vowel_count(a):
    count = 0
    for letter in a:
        if letter in 'aeiouAEIOU':
            count += 1
    return count

a = "Don't try buffer overflow attacks in Python!"

print(vowel_count(a))

#C1.25

def punctuation_remove(a):
    b = ''
    punctuation = ",.;:!?'"
    for letter in a:
        if letter not in punctuation:
            b = b + letter
    return b

a = "Don't try buffer overflow attacks in Python!"

print(punctuation_remove(a))

#C1.26

def arithmetric(a,b,c):
    if a+b == c: print(f"{a:d}+{b:d}={c:d}")
    elif a == b-c: print(f"{a:d}={b:d}-{c:d}")
    elif a*b == c: print(f"{a:d}*{b:d}={c:d}")
    else: print('no suitable arithmetric formula')

arithmetric(11,22,33)
arithmetric(11,22,11)
arithmetric(11,2,22)
arithmetric(11,22,10)

#C1.27

def factors(n):
    k = 1
    a = []
    b = []
    while k*k < n:
        if n%k == 0:
            a.append(k)
            b.append(n//k)
        k += 1
    if k*k == n:
        a.append(k)
    b.reverse()
    return a+b

a = factors(100)
print(a)

#C1.28

def norm(v, p=2):
    assert p!=0, 'p cannot be 0'
    t = 0
    for vi in v:
        t += vi**p
    return(t**(1/p))

print(norm([3,4]))
print(norm([3,4,5],3))

#P1.29

def words(suba,b):
    if len(suba) == 1:
        #print (''.join(list(map(str, b+suba))), end = ',')
        print (''.join(b+suba), end = ',')
        return
    else:
        for i in range(len(suba)):
            newa = [suba[j] for j in range(len(suba)) if j != i]
            words(newa,b+[suba[i]])

def all_combo(a):
    assert len(a)>0, 'string is null'
    words(list(a),[])

all_combo('catdog')

#P1.30

def d2c(n,c):
    newn = n/2
    if newn < 2:
        return
    c[0] += 1
    d2c(newn,c)

def divide2(n):
    assert type(n) == int and n > 0, 'number must be positive integer'
    c = [0]
    d2c(n,c)
    return c[0]

print(divide2(8))

#P1.31
