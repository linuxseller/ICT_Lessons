arr=[]
# for i in "0123456789":
#     for j in range(10**4):
#         n = int("12"+str(j)+"567"+i)
#         if n>10**10:
#             continue
#         if n%7777==0 and (n+1)%2==1:
from fnmatch import fnmatch
n=121025674
while True:
    if n>10**10:
        break
    if fnmatch(str(n), "12*567?") and (n+1)%2==1:
        arr.append(n)
    n+=7777
for i in sorted(arr):
    print(i, i//7777)

