f = open("27-A.txt")
n = int(f.readline())
a = []
for i in range(n):
    c = int(f.readline())
    a.append(c)

mxsm = mxln = 0
left = 0
sm = 0
for i in range(n):
    sm += a[i]
    if sm > 113:
        while sm%113!=0 and left < i:
            sm -= a[left]
            left+=1
        if sm > mxsm and i-left+1 > mxln:
            mxsm = sm
            mxln = i-left+1
print(mxln, mxsm)


