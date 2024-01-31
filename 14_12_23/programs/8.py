from itertools import product as pd

id=0

for i in pd(sorted("poliza"), repeat=6):
    id+=1
    if i.count('i')<=1 and i.count('a')==1 and i.count('z')<=2:
        print(i)
        print(id)
        break

#1815
