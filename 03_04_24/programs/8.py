even = "2460"
nums = "012345678"
last = "0234567"
count = 0
for a1 in even:
    for a2 in nums:
        for a3 in nums:
            for a4 in nums:
                for a5 in last:
                    n = a1+a2+a3+a4+a5
                    if n.count("3")<=1:
                        count += 1
print(count)
