data = open("26.txt").readlines()
n, ex_start, ex_end = map(int, data[0].split())
ex_start_cp = ex_start
data = data[1:] # sorted(data[1:], reverse=True)
first_candidates = []
for i in data:
    start, span = map(int, i.split())
    if start <= ex_start:
        first_candidates.append([start, span])

# first_viewer[start, end]
first_viewer = sorted(first_candidates, key=lambda x: x[1]-x[0], reverse=True)[0] 

# ex_start = ex_start + (span - (ex_start - start))
ex_start += (first_viewer[1] - (ex_start-first_viewer[0]))
count = 0
i=0
while ex_start<ex_end and i<len(data):
    start, span = map(int, data[i].split())
    if start<=ex_start:
        ex_start += (span-(ex_start-start))
        count += 1
    i += 1

print("-=----------")
print(first_viewer)
print(count, first_viewer[1]-ex_start_cp)

