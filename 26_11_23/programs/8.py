from itertools import product
words=0
count=1
for i in product("favorit", repeat=6):
    if(count%2==0):
        if(i[0]!='o'):
            if(i.count("r")==2):
                words+=1
    count+=1
print(words)
