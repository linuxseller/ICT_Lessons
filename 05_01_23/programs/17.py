with open("17.txt","r") as f:
    ls = [int(x.strip()) for x in f.readlines()]
    max_elem = -2000000
    count = 0
    maxx_sum = 0
    for i in ls:
        if len(set([x for x in str(abs(i))])) == 1 and len(str(abs(i))) == 3 and max_elem < i:
            max_elem = i
    for i in range(len(ls)-4):
        num1,num2,num3,num4,num5 = ls[i],ls[i+1],ls[i+2],ls[i+3],ls[i+4]
        tmp = [num1,num2,num3,num4,num5]
        state1 = ([str(i)[-1] == "4" for i in tmp].count(True) == 3)
        state2 = (max(tmp) % max_elem == 0)
        if state1 and state2:
            count += 1
            if maxx_sum < sum(tmp):
                maxx_sum = sum(tmp)
    print(count,maxx_sum)


