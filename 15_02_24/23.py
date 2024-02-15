def f(a,prev_com_a=False):
    if a>15:
        return 0
    if a==15:
        return 1
    if prev_com_a:
        return f(a*2, False)+f(a*3, False)
    return f(a-1, True)+f(a*2, False)+f(a*3, False)
print(f(3))
