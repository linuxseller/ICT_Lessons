def fits(a,b,c):
    global mx_321
    if [len(str(abs(x))) for x in [a,b,c]].count(5)==2 and (a%5==0 or b%5==0 or c%5==0) and a+b+c>mx_321:
        return True
    return False


data = list(map(int,open("17.txt").readlines()))

mx_321 = max(filter(lambda x: abs(x)%1000==321, data))
print(f"{mx_321=}")
c=0
mx=-10**9
for i in range(len(data)-2):
    a,b,c=data[i+0],data[i+1],data[i+2]
    if fits(a,b,c):
        c+=1
        mx = max(mx, a+b+c)
print(c, mx)
