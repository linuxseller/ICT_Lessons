sms = []

for n in range(3, 10000):
    s = "5" + "2"*n

    while "52" in s or "2222" in s or "1112" in s:
        if "52" in s:
            s=s.replace("52", "11", 1)
            s=s.replace("2222", "5", 1)
        else:
            s=s.replace("1112", "2", 1)
    sms.append(s.count("1") + s.count("2")*2 + s.count("5")*5)
print(max(sms))
