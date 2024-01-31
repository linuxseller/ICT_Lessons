def f(x,y,z,w):
    return not(w<=(not(x<=y))) and ((not x)<=((not y)==z))
print("x y z w f")
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if (f(x,y,z,w)==0):
                    print(x,y,z,w,0)
# ywzx
'''
y w z x f
0 1 1 1 0
1 1 0 0 1
0 1 1 0 1
'''
