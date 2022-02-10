#R4.1

def maxi(S, n, m):
    if n == 0:
        return m
    return maxi(S, n-1, max(m,S[n-1]))

S = [1,2,3,4,5,4,2]
print(maxi(S,len(S),S[len(S)-1]))

#R4.2

def power(x, n):
    if n == 0:
        return 1
    return x * power(x, n-1)

print(power(2, 5))

#R4.3

def power(x, n):
    if n == 1:
        return x
    partial = power(x, n//2)
    result = partial * partial
    if n%2 == 1:
        result *= x
    return result

print(power(2, 18))

#R4.4

def reverse(s, start, stop):
    if start >= stop - 1:
        return
    s[start], s[stop-1] = s[stop-1], s[start]
    reverse(s, start+1, stop-1)
    return

s = [4,3,6,2,6]
reverse(s,0,5)
print(s)

#R4.6

def harmonic(n):
    if n == 1:
        return 1
    
    return harmonic(n-1) + 1/n

print(harmonic(5))
