from itertools import product

for i in product("123", repeat=31+24+46):
    dst = list(i) 
    # print(dst)
    if dst.count("1")!=31 and dst.count("2")!=24 and dst.count("3")!=46:
        continue
    while "30" in dst or "3103" in dst or "1201" in dst:
        dst = dst.replace("1201", "03")
        dst = dst.replace("3103", "02")
        dst = dst.replace("30", "01")
    if dst[0]=="0":
        print(dst)
