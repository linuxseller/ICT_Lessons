arr = "aekpt4"
count = 0
flag = 0
id=0
for ch1 in arr:
    for ch2 in arr:
        for ch3 in arr:
            for ch4 in arr:
                for ch5 in arr:
                    for ch6 in arr:
                        for ch7 in arr:
                            id+=1
                            word = ch1+ch2+ch3+ch4+ch5+ch6+ch7
                            if flag and word!="pe4atka":
                                count+=1
                            if word=="apte4ka":
                                print(id)
                                flag=1
                            if word=="pe4atka":
                                flag=0
print(count)
