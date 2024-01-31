from functools import lru_cache

@lru_cache
def f(n):
    if n<3: return n
    if n%2==1: return f(n-1) + f(n-2) + 1
    sm = 0
    for i in range(1,n):
        sm += f(i)
    return sm

print(f(38))
