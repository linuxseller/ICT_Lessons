def f(x,y,z,w):
    return (y<=x) and (not z) and (w)

print("x y z w")
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if f(x,y,z,w)==1:
                    print(x,y,z,w)
"""
w x y z
1 0 0 0
1 1 0 0
1 1 1 0
"""
