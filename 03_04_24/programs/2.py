def f(x,y,z,w):
    return ((x<=z)<=y)or (not w)

print("x y z w")
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if f(x,y,x,w)==0:
                    print(x,y,z,w)
"
z x y w
1 0 0 1
0 1 0 1
0 0 0 1
1 1 0 1
"
