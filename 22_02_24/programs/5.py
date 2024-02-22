mxr=0
for n in range(50):
    r = bin(n)[2:]
    if r.count("1")%2==0:
        r+="0"
        r="11"+r[2:]
    else:
        r+="1"
        r="10"+r[2:]
    print(n,r)
    mxr = max(int(r,2), mxr)
print(mxr)
