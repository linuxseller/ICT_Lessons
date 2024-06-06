mx=0
for n in range(100,1000):
    r = int(str(((n//100) * (n%100//10))) + str((n%10 * (n%100//10))))
    if r==240: mx = max(n,mx)
print(mx)
