def is_multiple(n, m):
    if m == 0: return False
    return ( n%m == 0 )

print (is_multiple(3,0))
print (is_multiple(0,0))
print (is_multiple(3,2))
print (is_multiple(4,2))
print (is_multiple(-4,2))
