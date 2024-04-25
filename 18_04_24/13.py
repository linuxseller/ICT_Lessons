def ones(rightmost):
    ones = bin(212)[2:].count("1")
    ones += bin(170)[2:].count("1")
    ones += bin(120)[2:].count("1")
    ones += bin(rightmost)[2:].count("1")
    return ones

count = 0
for b4 in range(255):
    print(ones(b4))
    if b4&240==144 and ones(b4)>16:
        count += 1
        print(b4)
print(count)
