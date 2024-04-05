for n in range(1, 30):
    r = bin(n)[2:]
    if r.count("1")%2==0:
        r = "10" + r[:-2] + "00"
    else:
        r = "11" + r[:-2] + "11"
    print(n, r, int(r,2))

