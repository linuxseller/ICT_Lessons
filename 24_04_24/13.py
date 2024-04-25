def ct1s(b4):
    sm = bin(105)[2:].count("1")
    sm += bin(224)[2:].count("1")
    sm += bin(200)[2:].count("1")
    sm += bin(b4)[2:].count("1")
    return sm

count = 0
for b4 in range(255):
    if b4&224 == 224 and ct1s(b4)%4==0:
        count += 1
print(count)
