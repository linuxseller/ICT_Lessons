data =  list(map(int, open("17.txt").readlines()))
mmn = min(data)
mx = count = 0
for i in range(len(data)-1):
    a,b = data[i], data[i+1]
    if a%117==mmn or b%117==mmn:
        count += 1
        mx = max(mx, a+b)
print(count, mx)
