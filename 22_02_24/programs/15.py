def fits(a:int)->bool:
    for x in range(90,101):
        if not(x&79==0) and ((x&31==0)<=(not(x&a==0)))==0:
            return False
    return True

for i in range(200):
    if fits(i): print(i)
