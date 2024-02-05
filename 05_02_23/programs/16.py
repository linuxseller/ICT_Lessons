import sys
sys.setrecursionlimit(2**15)

def f(n):
    if n==1:
        return 2
    elif n>1:
        return f(n-1) * (3**(n%5)) / (3**(n%7))

print(f(1025))#/f(1030))
