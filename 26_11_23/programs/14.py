for x in "0123456789abcdefghijklm":
    if (int(f"1{x}1{x}1{x}1{x}1{x}",23)+int(f"20{x}24",23)+int(f"1{x}235",23)) % 22==0:
        print(x)
