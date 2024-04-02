data = list(map(int,open("txt.txt").readlines()))
k, n, data = data[0], data[1], data[2:]
mxml = -10**19
for i in range(len(data)-k*2):
    for j in range(i+k, len(data)):
        for l in range(j+k, len(data)):
            if (data[i] * data[j] * data[l]) % 2023 == 0:
                mxml = max(mxml, data[i]*data[j]*data[l])
print(mxml)


