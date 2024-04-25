def to3(n):
    eee = "012"
    res = ""
    while n!=0:
        res = eee[n%3] + res
        n//=3
    return res
mn = 111111110
for n in range(12,1000):
    r = to3(n)
    if n%3==0:
        r += r[-2:]
    else:
        r += to3((n%3)*5)
    num = int(r,3)
    if num>133:
        mn = min(mn, num)
print(mn)
