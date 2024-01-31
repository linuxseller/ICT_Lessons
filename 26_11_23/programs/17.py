file = open("../files/17.txt")
data = list(map(int, file.readlines()))
count = 0
mn_25 = 10**7
mxsum=0
for i in data:
    if i%100==25:
        mn_25=i

for i in range(len(data)-2):
    a,b,c=data[i], data[i+1], data[i+2]
    if list(map(len, map(str, map(abs, [a,b,c])))).count(2)==1:
        if a+b+c<mn_25:
            count+=1
            if mxsum<a+b+c:
                mxsum=a+b+c
print(mxsum, count)
