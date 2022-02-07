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

