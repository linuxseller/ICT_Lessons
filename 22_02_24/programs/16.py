import sys
sys.setrecursionlimit(2**15)

def f(n:int)->int:
    if n<5:
        return 4
    return 4*f(n-4)

print(f(4444)/f(4400))
