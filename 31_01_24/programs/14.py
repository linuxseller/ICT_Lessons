def sumof49(n):
    sum = 0
    while n!= 0:
        sum+=n%49
        n//=49
    return sum

e = 18*7**108 - 5*49**76 + 343**35 - 50
print(sumof49(abs(e)))
