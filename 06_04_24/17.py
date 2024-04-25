def fits(a,b,c, mx25):
    len3  = len(str(abs(a)))==4
    len3 += len(str(abs(b)))==4
    len3 += len(str(abs(c)))==4
    if len3<=2 and a+b+c<=mx25:
        return True
    return False
data = list(map(int, open("17.txt").readlines()))
mx25=max(filter(lambda x: abs(x)%100==25, data))
mx = count = 0
for i in range(len(data)-2):
    a,b,c = data[i],data[i+1],data[i+2]
    if fits(a,b,c, mx25):
        count += 1
        mx = max(mx, a+b+c)
print(count, mx)
