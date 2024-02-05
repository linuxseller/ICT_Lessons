mx_n = 0
mn_1 = 10**10
for i in range(100,1000):
    s="1"*i
    while "333" in s or "111" in s:
        s=s.replace("333","11").replace("111", "3")
    print(s, i)
    if int(s)>mx_n:
        mx_n = int(s)
        mn_1 = i

print(mn_1)
