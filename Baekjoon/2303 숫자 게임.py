from itertools import combinations

N = int(input())
numbers = [list(map(int, input().split())) for _ in range(N)]
result = 0
maxi = 0

for i in range(N):
    comb = list(combinations(numbers[i], 3))
    temp = 0
    for num in comb:
        temp = max(temp, sum(num) % 10)
    if temp >= maxi:
        result = i + 1
        maxi = temp
print(result)
