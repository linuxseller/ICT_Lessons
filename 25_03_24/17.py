data = list(map(int,open("17.txt").readlines()))
mx_3_sq = max(filter(lambda x: abs(x)%10==3, data))**2
count = 0
mx = -1000000
for i in range(len(data)-1):
    a,b = data[i], data[i+1]
    if len(list(filter(lambda x: abs(x)%10==3,[a,b])))==1:
        if a*a+b*b>=mx_3_sq:
            count += 1
            mx = max(mx, a*a+b*b)
print(mx_3_sq**0.5)
print(count, mx)
