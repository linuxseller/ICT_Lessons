def to5(n: int) -> str:
    eee = "01234"
    res=""
    while n!=0:
        res = eee[n%5] + res
        n//=5
    return res

for n in range(1,1000):
    if n%25==0:
        r = to5(n)[-3:] + to5(n)
    else:
        r = to5(n)+to5(n%25)
    if int(r, 5)>10000:
        print(n)
        break

