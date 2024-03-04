for p in range(16):
    for x in range(p):
        for y in range(p):
            for z in range(p):
                for w in range(p):
                    num1=z*(p**4)+x*(p**3)+y*(p**2)+x*(p**1)+7
                    num2=x*(p**4)+y*(p**3)+8*(p**2)+3*(p**1)+6
                    if ( num1 + num2  == w*(p**4)+z*(p**3)+x*(p**2)+6*(p**1)+4):
                        print(x*(p**3)+y*(p**2)+z*(p**1)+w)
