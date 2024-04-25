def f(x,y,z,w):
    return ((w or y) and (x <= (not z)) and (not w)) == 1

for a1 in range(2):
    for a2 in range(2):
        for a3 in range(2):
            for a4 in range(2):
                if f(a1,a2,a3,a4):
                    print(a1,a2,a3,a4)
"""
y z x w
1 0 0 0
1 0 1 0
1 1 0 0
"""
