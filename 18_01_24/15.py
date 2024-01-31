d = list(range(7,69))
c = list(range(29,101))

def f(x,a1, a2):
    a = list(range(a1,a2+1))
    (x in d) <= ((not(x in c) and not(x in a)) <= (not(x in d)))

for a1 in range(0,200):
    for a2 in range(a1,200):
        if all([f(x,a1,a2) for x in range(100)]):
            print(a1,a2, a2-a1)
