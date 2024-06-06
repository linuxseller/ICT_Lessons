def maxdel(n):
    for i in range(n-1,1,-1):
        if n%i==0:
            return i


for n in range(224466, 664423):
    if n%5==0 and n%7==0 and n%13==0 and \
            n%25!=0 and n%49!=0 and n%(13**2)!=0 and \
            maxdel(n)<=100000 and maxdel(n)%100==19:
        print(n, maxdel(n))
