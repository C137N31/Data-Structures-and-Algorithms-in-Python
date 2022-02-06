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
