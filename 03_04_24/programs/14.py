for x in range(79):
    num1 = 3*(80**3)+x*(80**2)+7*80+5
    num2 = 1*(80**3)+4*(80**2)+x*80+0
    num = num1+num2
    if num%17==0:
        print(num/17)
