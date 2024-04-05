data = open("24-1.txt").readline()
data = data.split("QW")
print(max(map(len, data))+2)
