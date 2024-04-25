f = [0]*2100
f[0] = 7
f[1] = 7
f[2] = 7
f[3] = 7
f[4] = 7
f[5] = 7
f[6] = 7
f[7] = 7
for n in range(8,2025):
    f[n]=n+1+f[n-2]
print(f[2024])
print(f[2023])
print(f[2024]-f[2020])
