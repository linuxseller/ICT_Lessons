def f(a,b,c,d):
    return (a<=b) and (c<=d) or (not c)


for a1 in range(2):
    for a2 in range(2):
        for a3 in range(2):
            for a4 in range(2):
                if f(a1,a2,a3,a4)==0:
                    print(a1,a2,a3,a4)
'''
b d c a
1 0 1 0
0 0 1 1
0 1 1 1
1 0 1 1
'''
