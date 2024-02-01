data = list(map(int, open("../data/17.txt").readlines()))
mn=10**10
count = 0
for i in range(len(data)-5):
    a1 = data[i+0]
    a2 = data[i+1]
    a3 = data[i+2]
    a4 = data[i+3]
    a5 = data[i+4]
    a6 = data[i+5]
    sm1, sm2, sm3 = a1+a2, a3+a4, a5+a6
    if sm2>sm1 and sm2>sm3:
        if sm1>0 and sm2>0 and sm3>0:
            count += 1
            if a3*a4<mn:
                mn = a3*a4

a1 = data[0]
a2 = data[1]
a3 = data[2]
a4 = data[3]
print(count, mn)
sm1, sm2 = a1+a2, a3+a4
if sm1>sm2:
    if sm1>0 and sm2>0:
        count += 1
        if a1*a2<mn:
            mn = a1*a2

print(count, mn)
a1 = data[len(data)-1]
a2 = data[len(data)-2]
a3 = data[len(data)-3]
a4 = data[len(data)-4]
sm1, sm2 = a1+a2, a3+a4
if sm1>sm2:
    if sm1>0 and sm2>0:
        count += 1
        if a1*a2<mn:
            mn = a1*a2
print(count, mn)
