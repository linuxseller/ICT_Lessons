import sys
sys.setrecursionlimit(100000)

def f(n:int)->int:
    if n==1:
        return 1
    return n*f(n-1)

print(f(2023)/f(2020))
