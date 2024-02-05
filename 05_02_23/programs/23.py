def f(a,ct):
    if a==80 and ct<=5:
        return True
    if a>80 or ct>5:
        return 0
    return f(a+1,ct+1) or f(a*2,ct+1) or f(a+a%4,ct+1)

count=0
for i in range(81):
    print(i, f(i,0))
    if f(i,0):
        count +=1
print(count)
