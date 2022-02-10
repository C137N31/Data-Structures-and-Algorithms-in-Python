#R4.1

def maxi(S, n, m):
    if n == 0:
        return m
    return maxi(S, n-1, max(m,S[n-1]))

S = [1,2,3,4,5,4,2]
print(maxi(S,len(S),S[len(S)-1]))

