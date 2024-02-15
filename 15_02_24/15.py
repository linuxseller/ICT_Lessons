def fits(a):
    for x in range(0,10000):
        if (((x&45>0) or (x&89>0))<=(x&a>0))==0:
            return False
    return True

for a in range(100000):
    if fits(a):
        print(a)
        break
