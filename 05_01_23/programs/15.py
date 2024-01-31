def div(a: int, b: int) -> bool:
    return a % b == 0

def bitchet(a):
    return bin(a)[2:].count("1")%2==0

for x in range(1000,-1000,-1):
    if bitchet(x)and(x in range(100,190)) and div(x,8):
        print(x)
