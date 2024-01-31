f = 10000*[0]
f[0]=1
f[1]=1
f[2]=1
for i in range(3,40):
    if i>2 and i%2==1:
        f[i] = f[i-1]-f[i-2]
        continue
    sm=0
    for j in range(1, i):
        sm+=f[j]
    f[i]=sm

print(f[39])
#41518080
