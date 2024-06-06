num = 51*7**12 - 7**3 - 22
digits = []
while num != 0:
    digits.append(num%7)
    num//=7
print(sum(digits))
