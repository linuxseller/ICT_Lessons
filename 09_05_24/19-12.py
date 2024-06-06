def piles(s):
    return s*3, s*2

def game(s):
    if s>=100: return "w"
    if any([game(i)=="w" for i in piles(s)]): return "p1"
    if any([game(i)=="p1" for i in piles(s)]): return "v1"
    if any([game(i)=="v1" for i in piles(s)]): return "p2"
    if all([game(i)=="p1" or game(i)=="p2" for i in piles(s)]): return "v2"
print("№19")
for s in range(1,100):
    if game(s)=="v1":
        print(s)

print("№20")
for s in range(1,100):
    if game(s)=="p2":
        print(s)
print("№21")
for s in range(1,100):
    if game(s)=="v2":
        print(s)
