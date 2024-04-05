from fnmatch import fnmatch
primes = [2,3,5,7,11,13,17,19,23,29,31,37, 41,43,47,53,59,61,71,73,79,83]
def sm(n):
    sum_ = 0
    while n!=0:
        sum_+=n%10
        n/=10
    return sum_
for x in range(931057,10**9):
    if  x%2801==0 and (sm(x) in primes) and fnmatch(str(x), "9*31?5*7"):
        print(x)
