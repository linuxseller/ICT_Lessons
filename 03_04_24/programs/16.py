# import sys
# from functools import *
# sys.setrecursionlimit(0xffff)
# @lru_cache(None)
# def f(n):
#     if n==1:
#         return 1
#     return n*f(n-1)-1
# print(f(1000)/f(997))
f = [0]*10000
f[1]=1
for n in range(2,1001):
    f[n]=n*f[n-1]-1
print(f[1000]/f[997])
