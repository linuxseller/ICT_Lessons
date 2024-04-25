s = open("24.txt").readline()
# s = "AABBCAB"
d = {"A":0,
     "B":0,
     "C":0,
     "D":0,
     "E":0,
     "F":0,
     "G":0,
     "H":0,
     "I":0,
     "J":0,
     "K":0,
     "L":0,
     "M":0,
     "N":0,
     "O":0,
     "P":0,
     "Q":0,
     "R":0,
     "S":0,
     "T":0,
     "U":0,
     "V":0,
     "W":0,
     "X":0,
     "Y":0,
     "Z":0
     }
for i in s:
    d[i]+=1
mn = 1000000000000000
minletter = ''
maxes = []
count = 0
mxs_count = max(d.values())
for k,v in d.items():
    if v==mxs_count:
        maxes += [k]
    if v<mn and v!=0:
        minletter = k
        mn = v
print(d, maxes, minletter)
for i in range(len(s)-2):
    a,b,c = s[i],s[i+1], s[i+2]
    if a == minletter or c == minletter:
        if b in maxes:
            count += 1
print(count)
