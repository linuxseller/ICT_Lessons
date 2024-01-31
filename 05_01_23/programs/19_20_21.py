from functools import lru_cache
def g(s):
    if 30 <= s <= 40:
        return s-2, s-4
    if 30 <= s+1 <= 40:
        return [s*2]
    return s+1,s*2
@lru_cache(None)
def h(s):
    if s >= 53: return "w"
    if any(h(i) == "w" for i in g(s)): return "a1"
    if all(h(i) == "a1" for i in g(s)): return "m1"
    if any(h(i) == "m1" for i in g(s)): return "a2"
    if all(h(i) == "a1" or h(i) == "a2" for i in g(s)): return "m2"

#19
for s in range(52,0,-1):
    if h(s) == "m1":
        print(s)
        break
print()
#20
for s in range(52,0,-1):
    if h(s) == "a2" and h(s) != "a1":
        print(s)
print()
#20
for s in range(52,0,-1):
    if h(s) == "m2":
        print(s)
