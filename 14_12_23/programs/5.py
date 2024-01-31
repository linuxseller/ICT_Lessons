for n in range(10000,1,-1):
    r=bin(n)[2:]
    if len(r)%2==0:
        r=r[:len(r)//2] + "1" + r[len(r)//2:]
    else:
        r=r
    r=int(r,2)
    if r<=26:
        print(r)
#26
