for x in "01234567890abcdef":
    a = int("12a"+x+"b3", 16)+int("2"+x+"d45", 16)+int("34E"+x+x+"5", 16)+int("d4"+x+"5f2e" ,16)
    if a%15==0:
        if bin(a)[2:].count("1")==14:
            print(a//15)
