def fits(a):
    for x in range(1,10000):
        if ((not (x%a==0)) <= ((x%28==0) <= (not (x%49==0)))) == False:
            return False
    return True

for a in range(1,10000):
    if fits(a):
        print(a)
