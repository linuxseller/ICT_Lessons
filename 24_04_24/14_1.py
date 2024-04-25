num = 3*2187**2020 + 3*729**2021 - 2*81**2022 + 27**2023 - 4*3**2024 - 2029

count = 0
while num != 0:
    print(num%27)
    if num%27>9:
        count += 1
    num //= 27
print(count)
