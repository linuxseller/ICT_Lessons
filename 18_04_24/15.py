count = 0

def f(r):
    for x in range(1,1000):
        for a in range(1,1000):
            if (( ( (x&108==0) or (x&60==0) ) <= (x&a==0) ) or (x&r==0))==0:
                return False
    return True
for r in range(10000):
    if f(r):
        count += 1
        print(count)
