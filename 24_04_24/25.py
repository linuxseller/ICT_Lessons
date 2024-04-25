from fnmatch import fnmatch

for i in range(158232272, 10**10, 2024):
    if i%2024==0:
        if fnmatch(str(i), "1*2322?2"):
            print(i, i//2024)

