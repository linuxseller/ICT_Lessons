sum = 0
for n in range(100_000_000):
    sum += int(bin(n)[2:]+bin(n%4)[2:], 10)
print(sum)
