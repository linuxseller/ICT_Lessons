def toSeven(n: int) -> str:
    lookup = "0123456"
    result = ""
    while n != 0:
        result = lookup[n%7] + result
        n //= 7
    return result

for n in range(1,1000):
    r = toSeven(n)
    r = r[-1]+r[1:-1]+r[0]
    r = int(r, 7)
    if r==2024:
        print(n, r)
# 656 2024
