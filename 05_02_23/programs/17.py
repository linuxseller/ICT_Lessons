def fits(a,b):
    return list(map(lambda x:len(str(x)), [a,b])).count(3)==1


data = list(map(int, open("../data/17.txt").readlines()))

mn_ln_3 = min(filter(lambda x:len(str(x))==3 and x%100==11, data))
count = 0
mx = 0

for i in range(len(data)-1):
    a,b=data[i],data[i+1]
    if fits(a,b):
        if abs(a-b)%mn_ln_3==0:
            count += 1
            mx = max(a+b, mx)

print(count, mx)
