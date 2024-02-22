def f(x,y,z,w):
    return (not(x==w and (not z))) and (y==x and (not w))

print("x y z w")
for a1 in range(2):
    for a2 in range(2):
        for a3 in range(2):
            for a4 in range(2):
                if f(a1,a2,a3,a4)==1:
                    print(a1,a2,a3,a4)
'''
z x y w
1 1 1 0
1 0 0 0
0 1 1 0
'''
