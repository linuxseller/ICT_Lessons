def fits(sx,ex):
    for x in range(200):
        if ((x not in range(sx,ex)) or (x not in p) and (x in q))==0:
            return False
    return True

mx = 0
p = range(23,45)
q = range(34,56)
for sx in range(100):
    for ex in range(sx, 100):
        if fits(sx,ex):
            mx = max(ex-sx, mx)
print(mx)
