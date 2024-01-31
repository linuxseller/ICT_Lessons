def fits(i):
    i = hex(i)[2:]
    for j in range(len(i)-1):
        if ord(i[j])<=ord(i[j+1]):
            return False
    return True

count = 0

for i in range(0x100, 0xFFF):
    if fits(i):
        print(hex(i))
        count += 1
for i in range(0x10000, 0xFFFFF):
    if fits(i):
        print(hex(i))
        count += 1
print(count)
