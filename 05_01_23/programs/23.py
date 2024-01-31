def f(a):
    if a==39:
        return 1
    if a%5==0 or a>39:
        return 0
    return f(a+2) + f(a+3) + f(2*a)

print(f(3))
# 1304
