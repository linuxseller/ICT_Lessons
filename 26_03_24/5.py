data = open("24-5.txt").readline()
mxlen = 0
count = 0
i = 0
vals = ["ABC", "BAC","CAB","CBA"]
prev = "   "
if data[0:3] in vals:
    i+=3
    prev = data[0:3]
while i<len(data)-1:
    a = data[i:i+3]
    if not(a in vals):
        mxlen = max(mxlen, count)
        count = 0
        i+=1
        continue
    i+=2
    prev=a
    count+=1
mxlen = max(count, mxlen)
print(mxlen)
