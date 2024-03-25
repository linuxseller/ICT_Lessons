from fnmatch import fnmatch

def fits(n:int):
    flag = False
    max2 = 0
    for i in range(2,n//2+1):
        if n%i==0:
            if flag:
                return False, 0
            flag = True
            max2 = i
    print(max2)
    return True, max2

for i in range(12021, 10**9):
    if fnmatch(str(i), "1?2*0*2?1"):
        fts, max2 = fits(i)
        if fts:
            print(fts)
            print(i, max2)
