def fits(a1,a2):
    for x in range(1000):
        if (((254<=x<=800) and (x not in range(a1, a2))) <= (410<=x<=823)) == False:
            return False
    return True
alskd=[]
for a1 in range(1000):
    for a2 in range(a1, 2000):
        if fits(a1,a2):
            alskd.append(a2-a1)
print(min(alskd))
