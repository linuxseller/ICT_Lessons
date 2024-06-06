data = open("24.txt").readline()
symb = data[0]
curlen = 0
maxlen = 0

for i in data[1:]:
    if i != symb:
        maxlen = max(maxlen, curlen)
        curlen = 0
        symb = i
    curlen += 1
maxlen = max(maxlen, curlen)
print(maxlen)
