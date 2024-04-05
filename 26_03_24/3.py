data = open("24-3.txt").readline()
mxlen = 0
count = 0
i = 0
while i<len(data)-2:
    a = data[i:i+3]
    if not(a[0]in"BC" and a[1]in"BC" and a[2] in "A"):
        mxlen = max(mxlen, count)
        count = 0
        i+=1
        continue
    i+=3
    count+=1*3
mxlen = max(mxlen, count)

print(mxlen)
