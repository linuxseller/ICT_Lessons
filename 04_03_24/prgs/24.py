data = open("../data/24.txt").readline()
print(data)
count = 0
lenn = 0
started = False
for i in range(len(data)):
    if data[i]=="A":
        started = True
    if data[i]=="B":
        lenn += 1
        started = False
        if lenn>=20:
            count += 1
        lenn = 0
    if started:
        lenn += 1

print(count)
