def f(x,y,z,w):
    return not(x<=y) or (x==z) or w

print("x y z w")
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                tmp = f(x,y,z,w)
                if tmp==0:
                    print(x,y,z,w,tmp)
"""
x w z y f()
1 0 0 1  0
0 0 1 1  0
0 0 1 0  0
"""
