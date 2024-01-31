f=[0]*30000

f[1]=5
for i in range(2,2030):
    f[i]=2*i+1+f[i-1]
print(f[2024]-f[2022])
