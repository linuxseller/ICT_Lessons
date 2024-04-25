for x in "0123456789abcdefghijkl":
    num = int("18"+x+"89957",22)+int("80"+x+"33",22)+int("521"+x+"6",22)
    if num%21==0:
        print(num//21)
