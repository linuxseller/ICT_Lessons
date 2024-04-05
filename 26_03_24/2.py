data = open("24-2.txt").readline()
data = data.split(".")
mx = 0
for i in range(len(data)-1):
    mx = max(mx, len(data[i]+data[i+1]))
print(mx)
