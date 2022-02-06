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
