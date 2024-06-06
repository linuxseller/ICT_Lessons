data = list(map(int, open("17.txt").readlines()))
min103 = min(list(filter(lambda x: x%103==0, data)))
count = mx = 0
for i in range(len(data)-1):
    a,b=data[i],data[i+1]
    if (a+b)%2==0 and (abs(a-b)%min103==0):
        count += 1
        mx = max(a+b, mx)

print(count, mx)
