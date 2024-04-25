def fits(a):
    for x in range(1000):
        for y in range(1000):
            if ((x*y<a)or(x<y)or(9<x))==0:
                return False
    return True

for x in range(100000):
    if fits(x): print(x); break
