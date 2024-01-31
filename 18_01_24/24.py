data = open("24.txt").readline()
vects = []
curvect = ""
ROs = 0
for i in range(len(data)-2):

    a,b,c = data[i], data[i+1], data[i+2]

    if a+b+c in "OROR":
        if ROs == 21:
            vects.append(curvect)
        ROs = 0
        curvect = ""

    if a+b == "RO":
        ROs += 1
    curvect += c

length = [len(a) for a in vects]

print(max(length))
