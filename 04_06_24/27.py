f = open("27A.txt")
n,m = map(int, f.readline().split())
a = []
for i in range(n):
    c = int(f.readline())
    d = c//6 if c%6==0 else c//6+1
    a.append(d)
max_pos1 = max_pos2 = 0
mx = sm = sum(a[0:2*m+1])
mx2 = sm2 = 0#sum(a[0:2*m+1])
for i in range(m+1,n-m):
    sm = sm - a[i-m-1] + a[i+m]
    if sm > mx:
        mx = sm
        max_pos1 = i
print(mx)
toremove=0
for i in range(m,n-m):
    if (max_pos1-2*m <= i and i <= max_pos1) or (max_pos1+2*m >= i and i >= max_pos1):
        sm2=0
        continue
    if sm2==0:
        sm2 = sum(a[i-m:i+m+1])
        toremove=a[i-m]
    else:
        sm2 = sm2 - toremove + a[i+m]
        toremove = a[i-m]
    if sm2 > mx2:
        mx2 = sm2
        max_pos2 = i
print(f"{mx=}, {mx2=}, {mx+mx2=}")
