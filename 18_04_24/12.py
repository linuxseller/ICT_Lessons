def get(a, i):
    i-=1
    return a[i]
def remove(a, i):
    i-=1
    return a[:i]+a[i+1:]
def write(a, i, c):
    i-=1
    return a[:i]+c+a[i+1:]

a = "ababbababbaa"
q = 1
i = 1
while q<4:
    c = get(a,i)
    if q==2:
        if c=="a":a=write(a,i,"b")
        else: q=1
    if q==3:
        if c=="b": a=write(a,i, "a")
        else: q = 1
    if q==1:
        a=remove(a,i)
        i = i-1
        if c=="a": q=3
        if c=="b": q=2
    i=i+1
    if i>len(a):
        q=4
print(a)
