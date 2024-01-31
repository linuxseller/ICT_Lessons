f = open("../data/24.txt")
data = f.read()

mx = 0

for L in range(len(data)):
    for R in range(L, len(data)):
        if data[L:R].count("AB")==21:
            if mx<R-L:
                mx=R-L
print(mx)

#95847081 4008
