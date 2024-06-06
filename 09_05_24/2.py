print("a b c")
for a in range(2):
    for b in range(2):
        for c in range(2):
            if (a and (not b) or c)==0:
                print(a,b,c)
"""
b a c
0 0 0 0
0 0 1 1
0 1 0 1
0 1 1 1
1 0 0 0
1 1 0 0

1 0 1 1
1 1 1 1
"""
