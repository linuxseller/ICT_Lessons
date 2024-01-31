for a in range ( 100,1000 ) :
    flag=True
    for y in range(1,1000):
        for x in range(1,1000):
            if (4*x+y<a)or(22<=x)==0:
                flag=False
                continue;
    if(flag):
        print(a)
        break
