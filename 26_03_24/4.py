data = open("24-4.txt").readline()
data = data.split("D")
data = [i for i in list(map(lambda x: x.split("FF"), data))]
print(data)
data = [i for i in list(map(lambda x: x.split("EE"), data))]
print(max(map(len, data)))
