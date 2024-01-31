for x in "0123456789abcdefghi":
    res=int("78"+x+"79643",19) + int("25"+x+"43",19) + int("63"+x+"5",19)
    if res%18==0:
        print(res/18)
