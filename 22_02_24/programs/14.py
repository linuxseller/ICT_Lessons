def to5(n:int)->str:
    eee = "01234"
    res = ""
    while n!=0:
        res = eee[n%5]+res
        n//=5
    return res
mx=0
for x in range(1000):
    for y in range(1000):
        n = 5**50 + 5**30 - 5**x - y - 5**y - x
        if(n<0):
            continue
        if to5(n).count("0")==10:
            print(to5(n), x, y, x*y)
            mx = max(mx, x*y)
print(mx)
