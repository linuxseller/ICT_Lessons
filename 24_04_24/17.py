data = list(map(int, open("17.txt").readlines()))
mx19 = max(list(filter(lambda x: x%19==0, data)))
mx = 0
count = 0
print(mx19, mx19/19)
for i in range(len(data)-1):
    a,b = data[i], data[i+1]
    if a>mx19 or b>mx19:
        count += 1
        mx = max(mx, a+b)
print(count, mx)
