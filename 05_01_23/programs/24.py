data = open("24.txt").read()
vowels = []
for i in range(len(data)):
    if data[i] in "AE":
        vowels.append(i)
print(max([vowels[i+100]-vowels[i] for i in range(len(vowels)-100)]))

