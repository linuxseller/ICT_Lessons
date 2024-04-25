def f(n):
    count_divs = 0
    divs = []
    for i in range(3,n//2+1,2):
        if n%i==0:
            if count_divs>=3:
                return False, []
            divs.append(i)
            count_divs+=1
    if count_divs!=3:
        return False, []
    return True, divs
for i in range(18782,18823):
    res, divs = f(i)
    if res:
        print(*divs)
