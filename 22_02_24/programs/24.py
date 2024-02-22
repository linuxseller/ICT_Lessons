d = open("../data/24.txt").readline()
breaks=[]
for i in range(len(d)-1):
    if ord(d[i])>ord(d[i+1]):
        breaks.append(i)
mx=0
for i in range(1, len(breaks)-100000):
    mx = max(breaks[i+100000]-breaks[i], mx)
print(mx)
