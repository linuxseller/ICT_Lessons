import re

pattern = r'33*21.7$'

for i in range(332107, 10**9):
    if re.match(pattern, str(i)) and i%2079==0:
        print(i, i/2079)
