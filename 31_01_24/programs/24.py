data = open("../data/24.txt").readline()
vowel_poss = []
for i in range(len(data)):
    if data[i] in "AEIOU":
        vowel_poss.append(i)
mx=0
for i in range(len(vowel_poss)-1):
    flag = True
    tmp = data[vowel_poss[i]:vowel_poss[i+1]]
    for g in range(len(tmp)-1):
        if ord(tmp[g])>ord(tmp[g+1]):
            flag = False
            continue
    if flag and mx<vowel_poss[i+1]-vowel_poss[i]:
        mx = vowel_poss[i+1]-vowel_poss[i]
print(mx)
