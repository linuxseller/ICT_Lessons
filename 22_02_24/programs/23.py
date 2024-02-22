def f(a,ct=0):
    if a>63 or ct==3:
        return 0
    if a==48:
        return 1
    return f(a-2, ct+1)+f(a*2, ct)+f(a*3, ct)
print(f(6))
