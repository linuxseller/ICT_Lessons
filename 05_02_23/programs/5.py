for n in range(1,1000):
    r = bin(n)[2:]
    if r.count("1")%2==1:
        r+="1"
    else:
        r+="0"
    r = int(r, 2)
    r = r*10+r%10
    if r>1200:
        print(r)
        break
