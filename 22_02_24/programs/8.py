import itertools as it

vowels = "oei"
count = 0
st=set()
for i in it.permutations("svstioe"):
    i = list(i)
    flag = False
    for j in range(len("sovesti")-1):
        if i[j] in vowels and i[j+1] in vowels:
            flag = True
    if not flag:
        st.add(''.join(i))
        print(i)
print(len(list(st)))
