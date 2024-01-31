from functools import lru_cache


def h(s):
    return (s+1), (s+4), (s*3)

@lru_cache(None)
def g(x):
    if x >= 202: return "w"
    if any(g(i)=="w" for i in h(x)): return "p1"
    if all(g(i)=="p1" for i in h(x)): return "v1"
    if any(g(i) == "v1" for i in h(x)): return "p2"
    if all(g(i) == "p2" or g(i) == "p1" for i in h(x)): return "v2"


# № 19
for s in range(1,202):
    if g(s) == "v1": print(s,g(s))
print("\n")
# № 20
for s in range(1,202):
    if g(s) == "p2": print(s,g(s))
print("\n")
# № 21
for s in range(1,202):
    if g(s) == "v2": print(s,g(s))
    
