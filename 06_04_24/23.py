def f(a):
    if a==3:
        return 1
    if a<3 or a==9 or a==6:
        return 0
    return f(a-1)+f(a-2)+f(a//3)
print(f(19))
