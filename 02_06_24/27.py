f = open("27B.txt")
n,L,R = map(int, f.readline().split())
data = sorted(list(map(int, f.readlines())))
data.sort()
left = 0
right = len(data) - 1
count = 0
prevmax = -1
# print(n,L,R)
while left < right:
    if (data[left] + data[right] ) > R:
        # count -= right - left
        right -= 1
    elif (data[left] + data[right]) < L:
        left += 1
    else:
        if prevmax==-1:
            for i in range(left, right):
                if data[i]+data[left]>=L:
                    prevmax = i
                    break
        elif prevmax < left:
            prevmax = left

            count += right - prevmax
        else:
            for i in range(prevmax, left, -1):
                if data[i]+data[left]>=L:
                    prevmax = i
                    break
            count += right - prevmax
        left += 1
print(count)
