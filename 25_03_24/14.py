for x in "0123456789abcde":
    num = int("123"+x+"5", 15)+int("1"+x+"233",15)
    if num%14==0:
        print(num/14)
