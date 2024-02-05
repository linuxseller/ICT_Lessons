count = res = 0
for a1 in "aepstuh":
    for a2 in "aepstuh":
        for a3 in "aepstuh":
            for a4 in "aepstuh":
                count += 1
                if count > 1000:
                    if a1!=a2 and a2!=a3 and a3!=a4:
                        print(count, a1+a2+a3+a4)
                        res += 1

print(res)
