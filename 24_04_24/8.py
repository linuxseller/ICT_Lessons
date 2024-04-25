#aprsu
#01234
#ppapa
print("sposob 1")
print(int("01010", 5)+1)
print("sposob 2")
count = 0
bukvi = "aprsu"
for a1 in bukvi:
    for a2 in bukvi:
        for a3 in bukvi:
            for a4 in bukvi:
                for a5 in bukvi:
                    count += 1
                    s = a1+a2+a3+a4+a5
                    if (s.count("u") in [0,1]) and not ( "aa" in [a1+a2, a2+a3, a3+a4, a4+a5] ):
                        print(s)
                        print(count)
