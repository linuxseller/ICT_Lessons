def f(n):
    res=""
    stm="0123"
    while n!=0:
        res=stm[n%4]+res
        n//=4
    return res

for n in range(1,10000):
    r=f(n)
    if n%4==0:
        r+=r[-2:]
    else:
        r+=f(n%4*2)
#    print(int(r,4))
    if int(r,4)<261 :
        print(int(r,4))
