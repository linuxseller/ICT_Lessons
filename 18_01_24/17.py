data = list(map(int, open("17.txt").readlines()))
mx_13 = -10**100
for i in data:
    if abs(i)%100==13 and mx_13<i:
        mx_13 = i
sm=0
count = 0
for i in range(len(data)-2):
    a,b,c = data[i], data[i+1], data[i+2]
    if (a%2==0 and b%2==0 and c%2==0) or (a//100==0 or b//100==0 or c//100==0):
        if a+b+c<=mx_13:
            sm    += a + b + c
            count += 1
print(count, sm//count)
