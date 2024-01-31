'''
x z y w   f()
1 1 0 0 | True
1 0 0 1 | True
1 0 1 1 | False
'''

def f(x,y,z,w):
    return x and (y<=z) and ((not y) <= ((not z)==w))

for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if f(x,y,z,w)==1:
                    print(x,y,z,w,"|",f(x,y,z,w))
