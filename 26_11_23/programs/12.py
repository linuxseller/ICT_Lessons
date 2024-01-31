for n in range(3,10000):
    s = "1" + "2"*n
    while "12" in s or "3322" in s or "2222" in s:
        if "12" in s:
            s=s.replace("12", "33", 1)
        if "22222" in s:
            s=s.replace("2222", "1", 1)
        if "3322" in s:
            s=s.replace("3322", "21", 1)
    arr = list(map(int, s))
    if sum(arr)==218:
        print(n)
    #print(arr)
