data = open("../data/24.txt").readline()
#data = "bbcdddeeefgggeeeddddk"
i=0
count=0
mx=0
while i<len(data)-2:
    a,b,c=data[i],data[i+1],data[i+2]
    if a==b==c:
        count += 3
        i+=3
    else:
        mx = max(mx, count)
        count = 0
        i+=1

mx = max(mx, count)
print(mx)
