for A in range(256):
    flag = True
    for r2 in range(256):
        if 252&r2==A:
            if bin(r2)[2:].count("1")<=3:
                flag = False
    if flag:
        print(A)
        break
