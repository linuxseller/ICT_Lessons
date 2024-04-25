data = open("24.txt").readline()
hexs = "0123456789ABCDEF"
maxlen = 0
curlen = 0
tmp = ""
for i in data:
    if i not in hexs:
        maxlen = max(maxlen, curlen)
        curlen = 0
        print(tmp)
        tmp = ""
        continue
    curlen += 1
    tmp+=i
print(maxlen)
