data = list(map(int, open("../data/17.txt").readlines()))

mn52 = min(filter(lambda x: abs(x)%52==0, data))
print(mn52)
count=0
mx=-10**11

for i in range(len(data)-2):
    a,b,c = data[i+0],data[i+1],data[i+2]
    if a%113+b%113+c%113 == mn52:
        count+=1
        mx=max(a+b+c, mx)
print(count, mx)
