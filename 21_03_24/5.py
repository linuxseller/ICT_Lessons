even = "02468ace"
for n in range(151, 1000):
    r=hex(n)[2:]
    r = r.replace("a", "1")
    count = 0
    for i in r:
        if i in even:
            count+=1
    if count>2:
        r+="b"
    else:
        r = "f"+r
    r = int(r, 16)
    if r>3500:
        print(n, r)
