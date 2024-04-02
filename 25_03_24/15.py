def fits(a:int)->bool:
    for x in range(1,1000):
        if ( ((x%2==0) <= (not(x%3==0)) ) or (x+a>=100) )==0:
            return False
    return True

for a in range(1,1000):
    if fits(a):
        print(a)
        break
