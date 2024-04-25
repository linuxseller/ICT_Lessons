from functools import *

def piles(s):
    s1, s2 = s
    return (s1*2,s2), (s1,s2*2), (s1, s2+1), (s1+1,s2)
@lru_cache(None)
def game(s):
    s1, s2 = s
    if s1+s2>=123: return "w"
    if any(game(i)=="w" for i in piles(s)): return "p1"
    if all(game(i)=="p1" for i in piles(s)): return "v1"
    if any(game(i)=="v1" for i in piles(s)): return "p2"
    if all(game(i)=="p2" or game(i)=="p1" for i in piles(s)): return "v2"
print("19 NUMED+ED")
for s2 in range(1,110):
    s = (13, s2)
    if game(s)=="v1":
        print(s)
print("20 NUMED+ED")
for s2 in range(1,110):
    s = (13, s2)
    if game(s)=="p2":
        print(s)
print("21 NUMED+ED")
for s2 in range(1,110):
    s = (13, s2)
    if game(s)=="v2":
        print(s)
