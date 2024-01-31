def to4(a):
    src = "0123"
    res = ""
    while a!=0:
        res = src[a%4] + res
        a//=4
    return res

for n in range(10000):
    e = to4(n)
    if len(e)%2==0:
        e = e[:len(e)//2] + "0" + e[len(e)//2:]
    if int(e)<=180:
        print(n)
