def check(a):
    for x in range(1000):
        for y in range(1000):
            if (3*x+y>a) and (y<x) and (x<30)==True:
                return False
    return True

for i in range(1000):
    if check(i):
        print(i)
