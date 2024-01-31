f = open("../data/17.txt")
data = list(map(int, f.readlines()))

mx = max(data)
count = 0
mn=100000000000000000000000
for i in range(len(data)-2):
    a,b,c=data[i],data[i+1],data[i-2]
    asda = a**2+b**2+c**2
    if asda>mx:
        count+=1
        if mn>asda:
            mn=asda
print(mn, count)
#95847081 4008
