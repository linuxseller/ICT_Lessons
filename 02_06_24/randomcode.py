def count_pairs(weights, L, R):
    weights.sort()
    left = 0
    right = len(weights) - 1
    count = 0

    while left < right:
        current_sum = weights[left] + weights[right]
        if L <= current_sum <= R:
            count += 1
            left += 1
            right -= 1
        elif current_sum < L:
            left += 1
        else:
            right -= 1

    return count
f = open("27B.txt")
n,L,R = map(int, f.readline().split())
data = sorted(list(map(int, f.readlines())))
result = count_pairs(weights, L, R)
print(result)
