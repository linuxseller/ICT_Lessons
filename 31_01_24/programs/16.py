#F(n)=42 при n>10 000;
#F(n)=2⋅n+F(n+3)+F(n+4)+F(n+6), если n≤10 000 и n — чётное;
#F(n)=−(n+F(n+1)+F(n+3)), если n≤10 000 и n — нечётное.

def f(n):
    if n>10_000:
        return 42
    elif n%2==0:
        return 2*n+f(n+3)+f(n+4)+f(n+6)
    return -(n+f(n+1)+f(n+3))

print(f(9996)-f(9994))
