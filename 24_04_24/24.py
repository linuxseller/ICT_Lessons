data = open("24.txt").readline()
nums = "6789"
lets = "ABC"

mxlen = 0
curlen = 0

for i in range(len(data)-1):
    a,b = data[i], data[i+1]
    if (a in nums and b in lets) or (a in lets and b in nums):
        curlen+=1
    else:
        mxlen = max(mxlen, curlen+1)
        curlen = 0
mxlen = max(mxlen, curlen+1)
print(mxlen)
