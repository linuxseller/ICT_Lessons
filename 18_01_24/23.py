def f(a, count):
    if count==68:
        return a
    return f(a+3, count+1) + f(a-2, count+1)

print(f(1,0))
